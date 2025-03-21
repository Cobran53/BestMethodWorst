Country = str
Criterion = str
Note = int

import numpy as np
from pyDecision.algorithm import bw_method
import yaml
from pprint import pprint
from tkinter import Tk, filedialog
from tkinter.messagebox import askquestion



class data_compile:
    def __init__(self) -> None:
        self.isDebug = True
        self.data: dict[Criterion, dict[Country, float|None]]
        # TODO

        with open("data.yaml", "r") as file:
            self.data = yaml.safe_load(file)

        if self.isDebug:
            pprint(self.data)
            print()
        
        self.fillEmptyLines()

        if self.isDebug:
            pprint(self.data)
            print()
        
        if self.askUserIfImport():
            self.importMICAndLIC()
        else:
            self.generateMostImportantCriteriaWeights()
            self.generateLeastImportantCriteriaWeights()
            self.saveMICAndLIC()

        self.generateActualWeights()
        self.calculateScoresByCountries()

        pprint({country: float(score) for country, score in self.countriesScores.items()})

    def askUserIfImport(self) -> bool: 
        response = askquestion("Importer les poids des critères", "Voulez-vous importer les poids des critères à partir d'un fichier YAML ?")
        if response == "cancel":
            print("Fermeture du programme.")
            exit()
        return response == "yes"

    def importMICAndLIC(self):
        root = Tk()
        root.withdraw()  # Masquer la fenêtre principale
        root.update()  # S'assurer que la fenêtre est correctement initialisée
        root.attributes('-topmost', True)
        file_path = filedialog.askopenfilename(title="Sélectionnez le fichier des poids des critères", filetypes=[("Fichiers YAML", "*.yaml")])
        
        if file_path:
            with open(file_path, "r") as file:
                weights = yaml.safe_load(file)
                self.mostImportantCriteriaNotes = weights["most_important_criteria"]
                self.leastImportantCriteriaNotes = weights["least_important_criteria"]
        else:
            print("Aucun fichier sélectionné. Fermeture du programme.")
            exit()

        root.destroy()          

    def fillEmptyLines(self):
        
        # Rejeter les critères où on a pas assez de donneés
        REJECT_CRITERIA_RATE = 0.5
        
        criteria_to_delete = []
        for criteria in self.data:
            country_data_count = sum(1 for country in self.data[criteria] if self.data[criteria][country])
            if country_data_count/len(self.data[criteria].keys()) < REJECT_CRITERIA_RATE:
                criteria_to_delete.append(criteria)

        for criteria in criteria_to_delete:
            print(f"Critère \"{criteria}\" supprimé : pas assez de données \n")
            del self.data[criteria]

        # Rejeter les pays où on a pas assez de données
        REJECT_COUNTRY_RATE = 0.5
        
        first_criteria = next(iter(self.data))

        countries_to_remove = []
        for country in self.data[first_criteria].keys():
            criteria_data_count = sum(1 for criteria in self.data if self.data[criteria][country] is not None)
            if criteria_data_count / len(self.data) < REJECT_COUNTRY_RATE:
                countries_to_remove.append(country)

        for country in countries_to_remove:
            print(f"Pays \"{country}\" supprimé : pas assez de données \n")
            for criteria in self.data:
                del self.data[criteria][country]

        # Remplacer par la moyenne dans les critères ou on a assez de données mais pas toutes 
        for criteria in self.data:
            values = [self.data[criteria][country] for country in self.data[criteria] if self.data[criteria][country] is not None]
            mean_value = np.mean(values) if values else 0
            for country in self.data[criteria]:
                if self.data[criteria][country] is None:
                    self.data[criteria][country] = mean_value

    def generateMostImportantCriteriaWeights(self) -> dict[Criterion, Note]:
        self.mostImportantCriteria: Criterion # nous déterminons qu'un des critères est le plus important
        self.mostImportantCriteriaNotes: dict[Criterion, Note] # pour chaque autre critère,
        # nous donnons une note sur leur importance par rapport au meilleur

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
        self.leastImportantCriteria: Criterion # idem pour le pire
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
            "least_important_criteria": self.leastImportantCriteriaNotes
            }, file)

    def generateActualWeights(self) -> dict[Criterion, float]:
        self.actualWeights: dict[Criterion, float] # utiliser l'exemple BWM pour générer les poids pour chaque critère

        criteria = sorted(self.mostImportantCriteriaNotes.keys())
        
        mic = np.array([self.mostImportantCriteriaNotes[crit] for crit in criteria])
        lic = np.array([self.leastImportantCriteriaNotes[crit] for crit in criteria])
        
        weights = bw_method(mic, lic, eps_penalty=1, verbose=self.isDebug)
        
        self.actualWeights = {crit: weights[i] for i, crit in enumerate(criteria)}

        pprint({criterion: float(weight) for criterion, weight in self.actualWeights.items()})

    def calculateScoresByCountries(self) -> dict[Country, float]:
        self.countriesScores = {
            country: sum(
                self.data[criteria][country] * weight for criteria, weight in self.actualWeights.items()
            ) for country in self.data[next(iter(self.data))].keys()
        }
        return self.countriesScores
    
A = data_compile()


# Faire une précision après avoir trouver le pays
# Ah, j'ai trouvé la france, donc maintenant je regarde la région française
# On fait ça que pour la france, mais au moins c'est développé


# faire en fonction de le localisation


# sauvegarde en .yaml

# 