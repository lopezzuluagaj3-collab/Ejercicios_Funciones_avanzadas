""" 6. Estación “LoopBus” – Simulador de pasajeros
Como conductor, quiero una función simular_viaje(pasajeros) que recorra con un for cada pasajero y muestre “Pasajero X a bordo”.
Si llega a 10 pasajeros, mostrar “Bus lleno” y detener el bucle. """

def simular_viaje():
    for i in range(0, 11):
        pasajero = input(F"{i}Ingrese el nombre de la su nombre: ")
        if i == 10: 
            print("Bus lleno")
            
simular_viaje()