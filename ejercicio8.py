""" 8. Cine “MovieLoop” – Calculadora de entradas
Como cajero, quiero una función calcular_entradas() que pida edades de los clientes hasta que se ingrese 0.
Aplicar precio:

    Menores de 12 → $5.000
    De 12 a 59 → $8.000
    Mayores de 60 → $4.000
    Usar un while y condiciones.
"""

def calcular_entradas():
    while True:
        print("Vienvenido al parque de diverciones\n"
            "Menores de 12 → $5.000\n"
            "De 12 a 59 → $8.000\n"
            "Mayores de 60 → $4.000\n"
            "--------------------------")
        edad = int(input("Ingrese su edad, si deseas que para de pedir edades ingresa `0`: "))
        if edad == 0:
            break
        
        elif edad <= 0 or edad >= 100:
            print("Edades no validas: ")
            
        elif edad >= 12 and edad <= 59:
            print("La entrada cuesta $8.000")
        
        elif edad < 12:
            print("La entrada cuesta $5.000")
        elif edad > 60:
            print("La entrada cuesta $4.000")
            
            
calcular_entradas()