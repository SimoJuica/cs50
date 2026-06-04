# Inicializar contadores
vehiculos_pesados = 0
vehiculos_ligeros = 0

# Pedir cantidad
while True:
    try:
        cantidad_vehiculos = int(input("¿Cuantos vehiculos desea registrar?: "))
        if cantidad_vehiculos > 0:
            break
        else:
            print("¡Cantidad invalida! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Cantidad invalida! Ingresa un entero positivo para continuar.")

# Recorrer cada vehiculo
for i in range(cantidad_vehiculos):
    print(f"\n--- Registro del Vehiculo {i + 1} ---")

    # Validar placa
    while True:
        placa = input("Ingrese la placa vehicular: ")
        if len(placa) >= 6 and " " not in placa:
            break
        else:
            print("¡Error de formato! La placa debe tener al menos 6 caracteres y no contener espacios.")

    # Validar capacidad
    while True:
        try:
            capacidad = int(input("Ingrese la capacidad de carga (en toneladas): "))
            if capacidad > 0:
                break
            else:
                print("¡Error logistico! Ingresa un numero entero positivo para la capacidad de carga.")
        except ValueError:
            print("¡Error logistico! Ingresa un numero entero positivo para la capacidad de carga.")

    # Clasificar (fuera del while, dentro del for)
    if capacidad > 55:
        vehiculos_pesados += 1
    else:
        vehiculos_ligeros += 1

# Resultado final (fuera del for)
print(f"\n¡La flota cuenta con {vehiculos_pesados} vehiculos Pesados y {vehiculos_ligeros} vehiculos Ligeros! ¡Rutas asignadas!")
    