# valores base
Plan_mensual = 25000
limpieza = 12000
valor_plan = 0
valor_limpieza = 0

# solicitar datos
edad = int (input("ingrese su edad: "))
afiliacion = input("ingrese tipo de afiliacion (B, E, P): ").upper()

# validar afiliacion 
if afiliacion not in ["B", "E", "P"]:
    print("tipo invalido")
    exit()

# --- Descuento del plan mensual ---
if edad > 60:
    Descuento_plan = 0.20
elif edad >= 46:
    if afiliacion in ["B","E"]:
        Descuento_plan = 0.05
    else: # Premium 
        Descuento_plan = 0.00
elif edad >= 26:
    if afiliacion == "B":
        Descuento_plan = 0.10
    else: # Estandar o premium 
        Descuento_plan = 0.05
else: # edad <= 25
    if afiliacion in ["B","E"]:
        Descuento_plan = 0.15
    else: # Premium
        Descuento_plan = 0.10

valor_plan = Plan_mensual * (1 - Descuento_plan)

# --- Descuento de la limpieza ---
if edad > 65:
    valor_limpieza = 0
elif afiliacion == "P":
    if edad >= 50:
        valor_limpieza = limpieza * (1 - 0.25) # 15% + 10%
    else:
        valor_limpieza = limpieza * (1 - 0.15)
else:
     valor_limpieza = limpieza 

# --- Mostrar resultado ---
print(f"valor del plan mensual: {int(valor_plan)}")
print(f"valor de la limpieza anual: {int(valor_limpieza)}")
print(f"total a pagar: {int(valor_plan + valor_limpieza)}")