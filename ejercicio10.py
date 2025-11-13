""" 10. Academia “CodeStart” – Tabla de multiplicar personalizada
Como estudiante, quiero una función tabla_multiplicar(numero) que use un for para mostrar la tabla del número dado hasta el 10.
Si el resultado es mayor de 50, mostrar también “Resultado alto”. """

""" def tabla_multiplicar():
    numero = int(input("Ingrese el numero que desee multiplicar: "))
    
    for i in range(1, 11):
        resultado = i * numero
        print(f"{numero} x {i} = {resultado}")
    if numero >= 50:
        print("alto resultado: ")
tabla_multiplicar() """


def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        if resultado > 50:
            print("Resultado alto")

num = int(input("Ingrese un número: "))
tabla_multiplicar(num)

