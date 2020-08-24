
def burbuja(lista):
    for n in range(len(lista) - 1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
    return lista

def shell(lista):
    mitad = len(lista) // 2

    while mitad > 0:
        for p in range(mitad):
            reducir_busqueda(lista, p, mitad)

        mitad = mitad // 2
    return lista

def reducir_busqueda(lista, inicio, salto):
    for i in range(inicio + salto, len(lista), salto):
        valor = lista[i]
        posicion = i

        while posicion >= salto and lista[posicion - salto] > valor:
            lista[posicion] = lista[posicion - salto]
            posicion = posicion - salto
        
        lista[posicion] = valor

def seleccion(lista):
    for n in range(len(lista) - 1, 0, -1):
        posicion_maxima = 0

        for l in range(1, n + 1):
            if lista[l] > lista[posicion_maxima]:
                posicion_maxima = l
        
        temp = lista[n]
        lista[n] = lista[posicion_maxima]
        lista[posicion_maxima] = temp
    return lista

def merge(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]

        merge_sort(primera_mitad)
        merge_sort(segunda_mitad)
        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i] < segunda_mitad[j]:
                lista[k] = primera_mitad[i]
                i += 1
            else:
                lista[k] = segunda_mitad[j]
                j += 1
            k += 1
        
        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i += 1
            k += 1
        
        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j += 1
            k += 1
    return merge

def cuentas(lista):
    maximo = max(lista) + 1
    conteo = [0] * maximo
    for n in lista:
        conteo[n] += 1
    i = 0
    for j in range(maximo):
        for k in range(conteo[j]):
            lista[i] = j
            i += 1
    return lista

def quick_sort(lista):
    quick_sort_auxiliar(lista, 0, len(lista) - 1)
    return lista

def quick_sort_auxiliar(lista, inicio, fin):
    if inicio < fin:
        punto_particion = particionar(lista, inicio, fin)

        quick_sort_auxiliar(lista, inicio, punto_particion - 1)
        quick_sort_auxiliar(lista, punto_particion + 1, fin)

def particionar(lista, inicio, fin):
    pivote = lista[inicio]

    izquierda = inicio + 1
    derecha = fin
    terminado = False

    while not terminado:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda += 1
        
        while lista[derecha] >= pivote and derecha >= izquierda:
            derecha -= 1
        
        if derecha < izquierda:
            terminado = True
        else:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
    
    lista[inicio], lista[derecha] = lista[derecha], lista[inicio]

    return derecha

def orderMethod(method, array, samples):
    samples = int(samples)
    if method == 'Burbuja':
        return burbuja(array[:samples])
    if method == 'Shell':
        return shell(array[:samples])
    if method == 'Merge':
        return merge(array[:samples])
    if method == 'Seleccion':
        return seleccion(array[:samples])
    if method == 'Cuentas':
        return cuentas(array[:samples]) 
    if method == 'QuickSort':
        return quick_sort(array[:samples])
    if method == 'PythonSort':
        return sorted(array[:samples])   
    
    
  