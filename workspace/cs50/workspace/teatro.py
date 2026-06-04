# teatro municipal

localidades_disponibles = 200
ventas_netas = 0
ejecutando = True

while ejecutando: 
    print("1. ver localidades")
    print("2. vender")
    print("3. devolver")
    print("4. historial")
    print("5. salir")
    try:
        opcion = int(input("seleccione una opcion (1-5): "))
        if opcion == 1:
            print(f"localidades disponibles: {localidades_disponibles}")
        elif opcion == 2:
            try:
                cantidad = int(input("¿cuantas localidades desea vender?:"))
                if cantidad > 0:
                    if cantidad <= localidades_disponibles:
                        localidades_disponibles -= cantidad
                        ventas_netas += cantidad
                        print(f"¡venta exitosa! se vendieron {cantidad} localidades.")
                    else:
                        print("¡error! No hay suficientes localidad disponibles.")
                else:
                    print("¡error! la cantidad debe ser mayor a 0.")
            except ValueError:
                print("error! ingrese un numero entero valido.")
        elif opcion == 3:
            try:
                cantidad = int(input("¿cuantas localidades desea devolver?:"))
                if cantidad > 0:
                    if localidades_disponibles + cantidad <= 200:
                        localidades_disponibles += cantidad
                        ventas_netas -= cantidad
                        print(f"¡devolucion exitosa! se reincorporaron {cantidad} localidad.")
                    else:
                        print("¡error! supera la capacidad maxima del teatro (200).")
                else:
                    print("error! la cantidad debe ser mayor a 0.")
            except ValueError:
                print("¡error! ingrese un numero entero valido.")
        elif opcion == 4:
            print(f"\nhistorial de ventas netas: {ventas_netas} localidades.")
        elif opcion == 5:
            print("\ngracias por utilizar nuestro software, hasta la proxima.")
            ejecutando = False
        else:
            print("¡opcion invalida! ingrese un numero entre 1 y 5.")
    except ValueError:
        print("¡error! solo ingrese numeros enteros en el menu.")