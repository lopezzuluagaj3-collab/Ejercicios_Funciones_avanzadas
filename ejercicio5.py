""" 5. Escuela “Aprende Más” – Promedio de notas
Como profesor, quiero una función promedio_notas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, de lo contrario “Reprobado”.
Debe repetirse para varios estudiantes usando un while. """

def promedio_notas():
    while True:
        suma = 0
        for i in range(1, 4):  
            while True:
                try:
                    nota = float(input(f"Enter your qualification {i}: "))
                    if 0 <= nota <= 5:
                        suma += nota
                        break
                    else:
                        print("The note must be between 0 and 5.")
                except ValueError:
                    print("Please enter a valid number.")
        
        promedio = suma / 3

        print(f"Your average is: {promedio:.2f}")
        if promedio < 3:
            print("Failed ")
        else:
            print("Approved ")

        salir = input("Do you want to calculate another average? (yes/no): ").lower()
        if salir != "yes":
            break

promedio_notas()