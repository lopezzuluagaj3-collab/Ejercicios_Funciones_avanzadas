
def calcular_propina():
    cuenta = int(input("Ingrese el total de la cuenta consumida: "))

    if cuenta >= 100000:
        propina = cuenta * 0.15
    else:
        propina = cuenta * 0.10

    print(f"La cantidad de propina que se debe dejar es: {propina}")

calcular_propina()
