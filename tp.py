import timeit
import matplotlib.pyplot as plt

def merge_sort(lista):
    if len(lista) < 2:
      return lista
    else:
        middle = len(lista) // 2
        left = merge_sort(lista[:middle])
        right = merge_sort(lista[middle:])
        return merge(left, right)
def merge(lista1, lista2):
    i, j = 0, 0
    result = []
    while(i < len(lista1) and j < len(lista2)):
        if ((lista1[i][0]/lista1[i][1]) < lista2[j][0]/lista2[j][1]):
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    result += lista1[i:]
    result += lista2[j:]
    return result

##Funciones Auxiliares

def calculadora_felicidad(batallas):
    batallas_ordenadas = merge_sort(batallas)
    suma = 0
    tiempo = 0
    for batalla in batallas_ordenadas:
        tiempo += batalla[0]
        suma += tiempo*batalla[1]
    return suma

def valores_optimos(ruta, suma):
    data = {
        "10.txt": 309600,
        "50.txt": 5218700,
        "100.txt": 780025365,
        "1000.txt": 74329021942,
        "5000.txt": 1830026958236,
        "10000.txt": 7245315862869,
        "100000.txt": 728684685661017
    }
   

    if ruta in data:
        coef = data[ruta]
        print("Algoritmo para ",batallas, "batallas:")
        print("El valor óptimo para", ruta, "es ", coef)
        print("El resultado es el óptimo" if suma == coef else "El resultado no es óptimo")
    else:
        print("No se encontró el archivo en la lista.")

def carga_datos(ruta):
    archivo = open("resultados/"+ruta,'r')
    lista = []
    lineas = archivo.readlines()
    for linea in lineas:
        linea = linea.replace('\n','') 
        if(linea!='T_i,B_i'):
            linea = linea.split(",")
            lista.append((int(linea[0]),int(linea[1])))
    archivo.close()
    return lista

def calcular_tiempos(archivos):
    tiempos = []
    for elemento in archivos:
        lista = carga_datos(elemento + ".txt")
        tiempo = timeit.timeit(lambda: calculadora_felicidad(lista), number=1)
        tiempos.append((elemento,tiempo))
    return tiempos


    
def graficar(tiempo):
    elemento_x = []
    elemento_y = []
    fig, ax = plt.subplots()
    # Dibujar puntos
    for elemento in tiempos:
        elemento_x.append(elemento[0])
        elemento_y.append(elemento[1])    
    ax.scatter(x = elemento_x, y = elemento_y)
    # Guardar el gráfico en formato png
    plt.savefig('diagrama-dispersion.png')
    # Mostrar el gráfico
    plt.show()


def main(batallas):
    ruta = batallas + ".txt"
    data = carga_datos(ruta)
    suma = calculadora_felicidad(data)
    valores_optimos(ruta, suma)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Batallas disponibles: 10, 50, 100, 1000, 5000, 10000, 100000")
        print("Ejemplo: python tp.py 100")
        print("Ejemplo: python tp.py graficar")
        sys.exit(1)
    elif(sys.argv[1] == "graficar"):
        archivos = ["10","50","100","1000","5000","10000","50000","100000"]
        tiempos = calcular_tiempos(archivos)
        graficar(tiempos)
    batallas = sys.argv[1]
    main(batallas)