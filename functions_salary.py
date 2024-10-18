import json
def compute_salary(hours_worked : int, contract_hours : int, hourly_rate : float) -> float:
    """ return the salary [€] that will be earned given 
    the following arguments : the hours worked [h], the contract hours [h], the hourly rate [€/h]
    """
    heure = 0
    salaire = 0
    while heure < hours_worked: #on sort de la boucle des que 
        if heure < contract_hours:
            salaire += hourly_rate
            heure +=1
        else :
            salaire += hourly_rate*1.5
            heure +=1
    salaire *= 4
    return(salaire) #donnees pour le mois


#def read_dict():

def o_JSON(chemin: str):
    with open(chemin, "r") as f:
        data = json.load(f)
    return data

def print_result_filiale(company_name :str, statistiques : float): 
    print('='*70)
    print(f"Statistique des salaires pour la filiale {company_name} : ")
    print(f"Salaire moyen : {statistiques[2]['salaire_mean']}€")
    print(f"Salaire minimum : {statistiques[1]['salaire_min']}€")
    print(f"Salaire maximum : {statistiques[0]['salaire_max']}€")
    print('='*70)

def stats_filiale():
    