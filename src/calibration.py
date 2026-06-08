KNOWN_WIDTH_CM = 8.56

distance_reference_cm = float(input("Distancia conhecida (cm): "))
width_pixels = float(input("Largura observada (pixels): "))

focal = (width_pixels * distance_reference_cm) / KNOWN_WIDTH_CM

print(f"\nFOCAL_LENGTH calculado = {focal:.2f}")
print("Copie esse valor para o main.py")
