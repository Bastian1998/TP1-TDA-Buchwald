def merge_sort_tiempo(lista):
    if len(lista) < 2:
      return lista
    else:
        middle = len(lista) // 2
        left = merge_sort_tiempo(lista[:middle])
        right = merge_sort_tiempo(lista[middle:])
        return merge(left, right)
def merge(lista1, lista2):
    i, j = 0, 0
    result = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i][0] < lista2[j][0]): #Ti, Bi (duración, importancia)
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    result += lista1[i:]
    result += lista2[j:]
    return result