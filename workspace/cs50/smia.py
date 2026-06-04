
alertas_altas = 0
alertas_normales = 0

# validacion inicial de ciclos de muestreo
while True:
    try:
        total_lecturas = int(input("¿cuantas lecturas de sensores desea procesar?"))
        if total_lecturas > 0: 
            break
        else:
            print("¡cantidad invalida! Ingrese un entero positivo para continuar.")
    except ValueError:
        print("¡cantidad invalida! Ingresa un entero positivo para continuar.")
        
# Bucle determinado para capturar datos individuales
for j in range(total_lecturas):
    print(f"\n--- Analisis de Sensor {j + 1} ---")

# validacion estricta de cadenas (codigo indentificador)
    while True:
         codigo_sensor = input("Ingrese el codigo indentificar del sensor: ")
         if len(codigo_sensor) >= 5 and " " not in codigo_sensor:
             break
         else:
             print("¡codigo invalido! Debe tener al menos 5 caracteres y no contener espacios.")

# validacion e insercion de rango numerico acotado con manejo de excepciones
while True:
    try:
        temp_actual = int(input("Ingrese la temperatura resgistrada (°C): "))
        if temp_actual >= -10 and temp_actual <= 50:
            break
        else:
            print("¡Error de lectura! Ingresa un numero entero valido dentro del rango termico permitido(-10 a 50).")
    except ValueError:
        print("¡Error de lectura! Ingresa un numero entero valido dentro del rango termico permitido (-10 a 50).")
# Bifurcacion condicional para clasificacion
if temp_actual > 30:
    alertas_altas += 1
else:
    alertas_normales += 1

# Presentaciones final estructurada
print(f"\n¡El invernadero registro {alertas_altas} lecturas ALTAS y {alertas_normales} lecturas NORMALES! ¡Ajuste de ventilacion ejecutado!")