""" 7. Panadería “Don Pancho” – Control de producción diaria
Como panadero, quiero una función hornear_pan(lotes) que use un for para indicar qué lote se está horneando.
Si el lote es divisible por 3, mostrar “Verificación de calidad”.
Al final, mostrar “Producción terminada”. """


def hornear_pan():
    lote = int(input("Ingrese la cantidad de lotes: "))
    for i in range(1, lote):
        i +=1
        print(f"Numeros de panes {i}")
        if i % 3 == 0:
            print(f"Verificacion de indentidad: ")
        elif i == lote:
            print(f"Producción terminada")
            
hornear_pan()