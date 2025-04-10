Country = str
Criterion = str
Note = int

import numpy as np
from pyDecision.algorithm import bw_method
import yaml
from pprint import pprint
from tkinter import Tk, filedialog
from tkinter.messagebox import askquestion
import csv
import os
from Visualization.interactive_map import generate_interactive_map

class data_compile:
    def __init__(self) -> None:
        self.isDebug = False
        self.data: dict[Criterion, dict[Country, float|None]] = {}
        self.rejectCriteriaRate = 0.5
        self.rejectCountryRate = 0.5

        print("Chargement des données...")

        data_dir = "./data"

        for filename in os.listdir(data_dir):
            if filename.endswith(".yaml"):
                criterion_name = os.path.splitext(filename)[0]
                with open(os.path.join(data_dir, filename), "r") as file:
                    self.data[criterion_name] = yaml.safe_load(file)

        if self.isDebug:
            pprint(self.data)
            print()
        if self.isDebug:
            pprint(self.data)
            print()

        if self.askUserIfImport():
            self.importMICAndLIC()
            self.fillEmptyLines()
        else:
            self.askRejectRates()
            self.fillEmptyLines()
            self.generateMostImportantCriteriaWeights()
            self.generateLeastImportantCriteriaWeights()
            self.saveMICAndLIC()

        self.generateActualWeights()
        self.calculateScoresByCountries()
        if self.isDebug:
            pprint({country: float(score) for country, score in self.countriesScores.items()})

    def replaceCountryByCountryCode(self):
        self.country_code_map = {}
        with open("country_code.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader)
            for row in reader:
                country_code = row[-1]
                for name in row[:-1]:
                    if name:
                        self.country_code_map[name.strip()] = country_code
        for criteria in self.data:
            updated_data = {}
            for country, value in self.data[criteria].items():
                country_code = self.country_code_map.get(country, country)
                if country_code == country:
                    print(f"Failed to replace country name: {country}")
            updated_data[country_code] = value
            self.data[criteria] = updated_data

    def askUserIfImport(self) -> bool: 
        response = askquestion("Importer les poids des critères", "Voulez-vous importer les poids des critères à partir d'un fichier YAML ?")
        if response == "cancel":
            print("Fermeture du programme.")
            exit()
        return response == "yes"
    
    def askRejectRates(self):
        print("Les critères de rejet actuels sont définis à 0.5 par défaut.")
        print("Le taux de rejet des critères détermine le % minimum de données nécessaires pour conserver un critère.")

        while True:
            try:
                reject_criteria_rate = float(input("Entrez le taux de rejet des critères (entre 0 et 1) : "))
                if 0 <= reject_criteria_rate <= 1:
                    self.rejectCriteriaRate = reject_criteria_rate
                    break
                else:
                    print("Veuillez entrer une valeur entre 0 et 1.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")

        print("Même fonctionnement pour le taux de rejet des pays.")

        while True:
            try:
                reject_country_rate = float(input("Entrez le taux de rejet des pays (entre 0 et 1) : "))
                if 0 <= reject_country_rate <= 1:
                    self.rejectCountryRate = reject_country_rate
                    break
                else:
                    print("Veuillez entrer une valeur entre 0 et 1.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")

    def importMICAndLIC(self):
        root = Tk()
        root.withdraw()
        root.update()
        root.attributes('-topmost', True)

        file_path = filedialog.askopenfilename(title="Sélectionnez le fichier des poids des critères", filetypes=[("Fichiers YAML", "*.yaml")])

        if file_path:
            with open(file_path, "r") as file:
                weights = yaml.safe_load(file)
                self.mostImportantCriteriaNotes = weights["most_important_criteria"]
                self.leastImportantCriteriaNotes = weights["least_important_criteria"]
                self.rejectCriteriaRate = weights.get("reject_criteria_rate", self.rejectCriteriaRate)
                self.rejectCountryRate = weights.get("reject_country_rate", self.rejectCountryRate)
        else:
            print("Aucun fichier sélectionné. Fermeture du programme.")
            exit()

        root.destroy()          

    def fillEmptyLines(self):
        criteria_to_delete = []

        for criteria in self.data:
            country_data_count = sum(1 for country in self.data[criteria] if country in self.data[criteria] and self.data[criteria][country] is not None)
            if country_data_count / len(self.data[criteria].keys()) < self.rejectCriteriaRate:
                criteria_to_delete.append(criteria)

        for criteria in criteria_to_delete:
            missing_percentage = 100 * (1 - country_data_count / len(self.data[criteria].keys()))
            print(f"Critère \"{criteria}\" supprimé : pas assez de données ({missing_percentage:.2f}% manquantes)")
            del self.data[criteria]

        first_criteria = next(iter(self.data))

        countries_to_remove = []

        for country in self.data[first_criteria].keys():
            criteria_data_count = sum(1 for criteria in self.data if country in self.data[criteria] and self.data[criteria][country] is not None)
            if criteria_data_count / len(self.data) < self.rejectCountryRate:
                countries_to_remove.append(country)

        for country in countries_to_remove:
            missing_percentage = 100 * (1 - criteria_data_count / len(self.data))
            print(f"Pays \"{country}\" supprimé : pas assez de données ({missing_percentage:.2f}% manquantes)")
            for criteria in self.data:
                self.data[criteria].pop(country, None)

        for criteria in self.data:
            values = [self.data[criteria][country] for country in self.data[criteria] if self.data[criteria][country] is not None]
            numeric_values = [v for v in values if isinstance(v, (int, float))]
            mean_value = np.mean(numeric_values) if numeric_values else 0
            for country in self.data[criteria]:
                if self.data[criteria][country] is None or self.data[criteria][country] == "None":
                    self.data[criteria][country] = mean_value

    def generateMostImportantCriteriaWeights(self) -> dict[Criterion, Note]:
        self.mostImportantCriteria: Criterion
        self.mostImportantCriteriaNotes: dict[Criterion, Note]
        criteria = sorted(self.data.keys())
        print("Veuillez choisir le critère le plus important :")

        for i, crit in enumerate(criteria, 1):
            print(f"{i}. {crit}")

        while True:
            try:
                choice = int(input("Entrez le numéro du critère le plus important : ")) - 1
                print()
                if 0 <= choice < len(criteria):
                    break
                else:
                    print("Choix invalide. Veuillez entrer un numéro correspondant au critère.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro valide.")

        self.mostImportantCriteria = criteria[choice]
        self.mostImportantCriteriaNotes = {self.mostImportantCriteria: 1}

        print("Évaluez l'importance de chaque critère par rapport au critère le plus important, de 1 à 9, avec \n" 
              "• 1 : le meilleur critère est aussi important que ce critère, \n"
              "• 9 : le meilleur critère est extremement plus important que ce critère.\n")
        
        for crit in criteria:
            if crit != self.mostImportantCriteria:
                while True:
                    try:
                        note = int(input(f"Évaluez l'importance de {crit} par rapport au critère le plus important (1-9) : "))
                        print()
                        if 1 <= note <= 9:
                            break
                        else:
                            print("Entrée invalide. Veuillez entrer un numéro entre 1 et 9.")
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer un numéro valide.")
                self.mostImportantCriteriaNotes[crit] = note

    def generateLeastImportantCriteriaWeights(self) -> dict[Criterion, Note]:
        self.leastImportantCriteria: Criterion
        self.leastImportantCriteriaNotes: dict[Criterion, Note]

        criteria = sorted(self.data.keys())

        print("Veuillez choisir le critère le moins important :")

        for i, crit in enumerate(criteria, 1):
            print(f"{i}. {crit}")

        while True:
            try:
                choice = int(input("Entrez le numéro du critère le moins important : ")) - 1
                if 0 <= choice < len(criteria):
                    break
                else:
                    print("Choix invalide. Veuillez entrer un numéro correspondant au critère.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro valide.")

        self.leastImportantCriteria = criteria[choice]
        self.leastImportantCriteriaNotes = {self.leastImportantCriteria: 1}

        print("Évaluez l'importance de chaque critère par rapport au critère le moins important, de 1 à 9, avec \n" 
              "• 1 : le pire critère est aussi important que ce critère, \n"
              "• 9 : le pire critère est extrêmement moins important que ce critère.\n")
        
        for crit in criteria:
            if crit != self.leastImportantCriteria:
                while True:
                    try:
                        note = int(input(f"Évaluez l'importance de {crit} par rapport au critère le moins important (1-9) : "))
                        print()
                        if 1 <= note <= 9:
                            break
                        else:
                            print("Entrée invalide. Veuillez entrer un numéro entre 1 et 9.")
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer un numéro valide.")
                self.leastImportantCriteriaNotes[crit] = note

    def saveMICAndLIC(self):
        with open("criteria_weights.yaml", "w") as file:
            yaml.dump({
                "most_important_criteria": self.mostImportantCriteriaNotes,
                "least_important_criteria": self.leastImportantCriteriaNotes,
                "reject_criteria_rate": self.rejectCriteriaRate,
                "reject_country_rate": self.rejectCountryRate
            }, file)

    def generateActualWeights(self) -> dict[Criterion, float]:
        self.actualWeights: dict[Criterion, float]

        criteria = sorted(self.mostImportantCriteriaNotes.keys())
        mic = np.array([self.mostImportantCriteriaNotes[crit] for crit in criteria])
        lic = np.array([self.leastImportantCriteriaNotes[crit] for crit in criteria])
        weights = bw_method(mic, lic, eps_penalty=1, verbose=True or self.isDebug)

        self.actualWeights = {crit: weights[i] for i, crit in enumerate(criteria)}

        if self.isDebug:
            pprint({criterion: float(weight) for criterion, weight in self.actualWeights.items()})

    def calculateScoresByCountries(self) -> dict[Country, float]:
        self.countriesScores = {
            country: sum(
                float(self.data[criteria].get(country, 0) or 0) * weight for criteria, weight in self.actualWeights.items()
            ) for country in self.data[next(iter(self.data))].keys()
        }

        min_score = min(self.countriesScores.values())
        self.countriesScores = {country: score - min_score for country, score in self.countriesScores.items()}

        with open("./Visualization/current_criteria_weights.yaml", "w") as file:
            yaml.dump({
                "most_important_criteria": self.mostImportantCriteriaNotes,
                "least_important_criteria": self.leastImportantCriteriaNotes,
                "reject_criteria_rate": self.rejectCriteriaRate,
                "reject_country_rate": self.rejectCountryRate
            }, file)

        print("Le fichier de poids current_criteria_weights.yaml a été créé avec succès.")

        with open("./Visualization/output.yaml", "w") as file:
            yaml.dump({country: float(score) for country, score in self.countriesScores.items()}, file)
            
        print("Le fichier de données output.yaml a été créé avec succès.")
        generate_interactive_map()
        return self.countriesScores
    
A = data_compile()
