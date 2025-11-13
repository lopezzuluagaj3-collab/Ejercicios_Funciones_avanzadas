"""4. Banco “PythonBank” – Evaluador de crédito
Como asesor financiero, quiero una función evaluar_credito(ingresos, edad) que:

    Apruebe el crédito si los ingresos son mayores de 2 millones y la edad está entre 25 y 60.
    Si no cumple, mostrar “Crédito rechazado”.
    Usar condicionales dentro de la función.
"""
def evaluar_credito():
    credit = input("enter you credit: ")
    while not credit.isdigit():
        print("Invalid data entered: ")
        credit = input("enter you credit: ")
    credit = int(credit)
    
    aga = input("Enter how old you are: ")
    while not aga.isdigit():
        print("Invaled data entered: ")
        aga = input("Enter how old you are: ")
    aga = int(aga)
    
    if credit < 2000000 or aga <= 24:
        print("you loan cannot be approved: ")
    else:
        print("you loan was approved: ")
        
evaluar_credito()