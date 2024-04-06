import timeit
import matplotlib.pyplot as plt
from ordenadoPorCociente import merge_sort_cociente
from ordenadoPorPeso import merge_sort_peso
from ordenadoPorDuracion import merge_sort_tiempo

def calculadora_impacto(batallas, algoritmo):
    batallas_ordenadas = []
    if(algoritmo == "cociente"):
        batallas_ordenadas = merge_sort_cociente(batallas)
    elif(algoritmo == "peso"):
        batallas_ordenadas = merge_sort_peso(batallas)
    elif(algoritmo == "tiempo"):
        batallas_ordenadas = merge_sort_tiempo(batallas)
    else:
        batallas_ordenadas = merge_sort_cociente(batallas)
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
        print("El resultado del algorithmo es ", suma)
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
        tiempo = timeit.timeit(lambda: calculadora_impacto(lista, "cociente"), number=1)
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
    plt.ylabel('Tiempo de ejecucion')
    plt.xlabel('Input de datos(cantidad batallas)')
    plt.title('Gráfico cantidad batallas vs tiempo')
    # Guardar el gráfico en formato png
    plt.savefig('diagrama-dispersion.png')
    # Mostrar el gráfico
    plt.show()


def main(batallas, algoritmo):
    ruta = batallas + ".txt"
    data = carga_datos(ruta)
    suma = calculadora_impacto(data, algoritmo)
    valores_optimos(ruta, suma)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Batallas disponibles: 10, 50, 100, 1000, 5000, 10000, 100000")
        print("Ejemplo: python tp.py 100 cociente/ peso/ tiempo")
        print("Ejemplo: python tp.py graficar")
        sys.exit(1)
    elif(sys.argv[1] == "graficar"):
        archivos = ["10","20","30","40","50","60","70","80","90","100","1000","2000","3000","4000","5000","10000","20000","30000","40000","50000","60000","70000","80000","90000","100000"]
        tiempos = calcular_tiempos(archivos)
        graficar(tiempos)
    elif (sys.argv[2] in ["cociente","peso","tiempo"]):
        batallas = sys.argv[1]
        algoritmo = sys.argv[2]
        main(batallas, algoritmo)
    else:
        batallas = sys.argv[1]
        main(batallas, "cociente")