

def aplicar_descuentos():
    total = 0

    print("Escoge todos los productos que desees. Para dejar de agregar, presiona 0.")

    while True:
        producto = int(input("Ingresa el precio del producto: "))

        if producto == 0:
            break  

        if producto >= 50000:
            producto = producto * 0.1
            print(f"Descuento aplicado. Nuevo precio: {producto}")
        else:
            print(f"Precio sin descuento: {producto}")

        total += producto  

    print(f"\nEl total a pagar por todos los productos es: {total}")

aplicar_descuentos()
