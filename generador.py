import random

# Función para generar un número en el formato "T_i,B_i"
def generar_numero():
    return f"{random.randint(100, 999)},{random.randint(100, 999)}"

# Función para generar y guardar números en un archivo
def generar_archivo(numero_de_numeros):
    numeros = [generar_numero() for _ in range(numero_de_numeros)]
    with open(f"{numero_de_numeros}.txt", "w") as archivo:
        archivo.write("T_i,B_i\n")  # Escribir encabezado
        for numero in numeros:
            archivo.write(numero + "\n")
    print(f"Se han generado y guardado {numero_de_numeros} números en 'numeros_{numero_de_numeros}.txt'.")

# Generar archivos para diferentes cantidades de números
for cantidad in range(10000, 110000, 10000):
    if(cantidad==10000 or cantidad == 50000 or cantidad == 100000):
        continue
    generar_archivo(cantidad)