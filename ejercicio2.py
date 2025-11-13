def repeticiones():
    series = input("Ingrese el numero de serie en la que va: ")
    while not series.isdigit():
        print("Dijito ingresado no valido: ")
        series = input("Ingrese el numero de serie en la que va: ") 
    series = int(series)
    for i in range(1, series + 1 ):
        if i % 2 == 0:
            print(f"Exelente forma: {i}")
        else:
            print(f"Manten el ritmo {i}")
            

repeticiones()