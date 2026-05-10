# ruleta de casino
import random

# solicitar apuesta
Apuesta = input("Apuesta a par o impar? (P/I): ").upper()

# validar apuesta 
if Apuesta not in ["P", "I"]:
    print("Apuesta invalida")
    exit()

# generar numero al azar
numero = random.randint(0, 36)
print(f"El numero fue: {numero}")

# --- determinar resultado ---
if numero == 0:
    print("¡Perdiste! Gano la casa.")
elif numero % 2 == 0 and Apuesta == "P":
    print(f"¡Ganaste! {numero} es par.")
elif numero % 2 != 0 and Apuesta == "I":
    print(f"¡Ganaste! {numero} es impar.")
else:
    print(f"¡Perdiste! {numero} no era tu Apuesta.")