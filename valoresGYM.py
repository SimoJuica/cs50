# valores GYM
Plan_mensual = 18000
Clases = 8000

# solicitar datos 
edad = int(input("ingrese su edad:"))
afiliacion = input("ingrese tipo de plan(B, E, P): ").upper()

# validar plan
if afiliacion not in ["B", "E", "P"]:
    print("plan invalido")
    exit()

# --- Descuento de Membresia anual ---
if edad > 60:
    Descuento_plan = 0.25
elif edad >= 36:
    if afiliacion in ["B", "E"]:
        Descuento_plan = 0.05
    else: # premium
        Descuento_plan = 0.00
elif edad >= 19:
    if afiliacion =="B":
        Descuento_plan = 0.08
    else: # Estandar o premium
        Descuento_plan = 0.05
else: # edad <= 18
    if afiliacion in ["B", "E"]:
        Descuento_plan = 0.20
    else:
        Descuento_plan = 0.12
valor_plan = Plan_mensual * (1 - Descuento_plan)

# --- Descuento de las Clases ---
if edad > 70:
    valor_clases = 0
elif afiliacion == "P":
    if edad >= 55:
        valor_Clases = Clases * (1 - 0.35) # 20% + 15%
else:
    valor_Clases = Clases * (1 - 0.20)

# --- Mostrar resultado ---
print(f"Membresia:{int(valor_plan)}")
print(f"Clases: {int(valor_Clases)}")
print(f"Total: {int(valor_plan + valor_Clases)}")