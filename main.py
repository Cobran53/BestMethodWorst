Country = str
Criterion = str
Note = int

import numpy as np

from pyDecision.algorithm import bw_method

class data_compile:
    def __init__(self) -> None:
        self.data: dict[Criterion, dict[Country, float|None]]
        # TODO

        self.data = {
            "Critère 1": {
                "Pays A": 0.8,
                "Pays B": 0.6,
                "Pays C": 0.9, 
                "Pays sans données": None,
            },
            "Critère 2": {
                "Pays A": 0.7,
                "Pays B": 0.8,
                "Pays C": 0.6, 
                "Pays sans données": None,
            },
            "Critère 3": {
                "Pays A": 0.9,
                "Pays B": 0.5,
                "Pays C": 0.7, 
                "Pays sans données": None,
            }, 
            "Critère sans données": {

            }
        }
        """self.data = pd.DataFrame({
            "Critère 1": {
            "Pays A": 0.8,
            "Pays B": 0.6,
            "Pays C": 0.9, 
            "Pays sans données": None,
            },
            "Critère 2": {
            "Pays A": 0.7,
            "Pays B": 0.8,
            "Pays C": 0.6, 
            "Pays sans données": None,
            },
            "Critère 3": {
            "Pays A": 0.9,
            "Pays B": 0.5,
            "Pays C": 0.7, 
            "Pays sans données": None,
            }
        }).T*/"""
        self.generateMostImportantCriteriaWeights()
        self.generateLeastImportantCriteriaWeights()
        self.generateActualWeights()
        self.calculateScoresByCountries()

        print(self.countriesScores)

    def fillEmptyLines(self):
        
        # Rejeter les critères ou on a pas assez de donneés
        REJECT_CRITERIA_RATE = 0.5
        


        # Rejeter les pays où on a pas assez de données
        REJECT_COUNTRY_RATE = 0.5
        
        first_criteria = next(iter(self.data))

        countries_to_remove = []
        for country in self.data[first_criteria].keys():
            filled_criteria_count = sum(1 for criteria in self.data if self.data[criteria][country] is not None)
            if filled_criteria_count / len(self.data) < REJECT_COUNTRY_RATE:
                countries_to_remove.append(country)

        for country in countries_to_remove:
            for criteria in self.data:
                del self.data[criteria][country]
        
        

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
              "• 9 : le meilleur critère est extremement plus important que ce critère)\n")
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

        with open("most_important_criteria_weights.txt", "w") as file:
            for crit, note in self.mostImportantCriteriaNotes.items():
                file.write(f"{crit}: {note}\n")

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
              "• 9 : le pire critère est extrêmement moins important que ce critère)\n")
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

        with open("least_important_criteria_weights.txt", "w") as file:
            for crit, note in self.leastImportantCriteriaNotes.items():
                file.write(f"{crit}: {note}\n")

    def generateActualWeights(self) -> dict[Criterion, float]:
        self.actualWeights: dict[Criterion, float] # utiliser l'exemple BWM pour générer les poids pour chaque critère

        criteria = sorted(self.mostImportantCriteriaNotes.keys())
        
        mic = np.array([self.mostImportantCriteriaNotes[crit] for crit in criteria])
        lic = np.array([self.leastImportantCriteriaNotes[crit] for crit in criteria])
        
        weights = bw_method(mic, lic, eps_penalty=1, verbose=True)
        
        self.actualWeights = {crit: weights[i] for i, crit in enumerate(criteria)}

        print(self.actualWeights)

    def calculateScoresByCountries(self) -> dict[Country, float]:
        self.countriesScores = {
            country: sum(
                self.data[criteria][country] * weight for criteria, weight in self.actualWeights.items()
            ) for country in self.data[next(iter(self.data))].keys()
        }
        return self.countriesScores
    
A = data_compile()