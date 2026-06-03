# Dado
import random

# Generar dados
Dado_usuario = random.randint(1, 6)
Dado_computadora = random.randint(1, 6)

# Mostrar resultado
print(f"Tu Dado: {Dado_usuario}")
print(f"DAdo computadora: {Dado_computadora}")

# --- Determinar ganador ---
if Dado_usuario == 6:
    print("¡Sacaste 6! Ganaste automaticamente.")
elif Dado_usuario > Dado_computadora:
    print(f"¡Ganaste! {Dado_usuario} es mayor que {Dado_computadora}.")
elif Dado_computadora > Dado_usuario:
     print(f"Perdiste. La computadora saco {Dado_computadora}.")
else:
    print("¡Empate!")