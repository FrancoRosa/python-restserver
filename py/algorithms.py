##-01Insert
def ordenamientoPorInsercion(A):
    for j in range(1, len(A)):
        key = A[j] 
        i = j-1
        while i >= 0 and A[i] > key : 
            A[i + 1] = A[i] 
            i = i - 1
        A[i+1] = key 
    return A  
# ordenamientoPorInsercion(unaLista) 

##-02Shell
def ordenamientoDeShell(A):
    n = len(A) 
    gap = n//2
    while gap > 0: 
        for i in range(gap,n): 
            temp = A[i] 
            j = i 
            while  j >= gap and A[j-gap] >temp: 
                A[j] = A[j-gap] 
                j -= gap 
            A[j] = temp 
        gap //= 2
    return A
# ordenamientoDeShell(unaLista)

##-03Bubble
def ordenamientoBurbuja(A):
    for i in range(len(A)):         
        for j in range(0, len(A)-i-1):             
            if A[j] > A[j+1] : 
                A[j], A[j+1] = A[j+1], A[j] 
    return A
# ordenamientoBurbuja(unaLista)

##-04Merge
import math
def mergeSort(A, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSort(A, l, m)
        mergeSort(A, m + 1, r)
        merge(A, l, m, r)
    return A

def merge(A, l, m, r):
    nL = m - l + 1
    nR = r - m
    L = [0] * (nL + 1)
    R = [0] * (nR + 1)
    for i in range(0, nL):
        L[i] = A[l + i]
    for j in range(0, nR):
        R[j] = A[m + 1 + j]
    L[nL] = math.inf
    R[nR] = math.inf
    i = 0
    j = 0
    for k in range(l, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
# ordenamientoPorMezcla(unaLista)
 
##-05Quicksort
def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
    return A

def partition(A, p, r):
    x = A[r]
    i = (p-1)         
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
 
    A[i+1], A[r] = A[r], A[i+1]
    return (i+1)

# ordenamientoRapido(unaLista)
 
##-06Bucket
def bucket_sort(inpvalue):
    largest = max(inpvalue)
    length = len(inpvalue)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(inpvalue[i]/size)
        
        if j != length:
            buckets[j].append(inpvalue[i])
        else:
            buckets[length - 1].append(inpvalue[i])
 
    for i in range(length):
        insertion(buckets[i])
 
    res = []
    
    for i in range(length):
        res = res + buckets[i]
 
    return res

# bucket_sort(array)


##-07Radix
def countingSort(arr, exp1): 
   
    n = len(arr) 
   
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
   
    # initialize count array as 0 
    count = [0] * (10) 
   
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
   
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
   
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
    return arr
# radixSort(arr)
 
##-08heap
def heapify(A, n, i): 
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  
    if l < n and A[i] < A[l]: 
        largest = l 
    if r < n and A[largest] < A[r]: 
        largest = r 
    if largest != i: 
        A[i],A[largest] = A[largest],A[i]  
        heapify(A, n, largest) 
    
def heapSort(A): 
    n = len(A) 
    for i in range(n//2 - 1, -1, -1): 
        heapify(A, n, i) 
    for i in range(n-1, 0, -1): 
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0) 
    return A
# heapSort(arr) 

##-09Count
def countingSort(arr, exp1): 
   
    n = len(arr) 
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
   
    # initialize count array as 0 
    count = [0] * (10) 
   
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
   
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
   
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
    
    return arr
# Driver code to test above
# radixSort(arr)
 
##-10bin
def insertion(inpvalue):
    for i in range(1, len(inpvalue)):
        temp = inpvalue[i]
        j = i - 1
        while (j >= 0 and temp < inpvalue[j]):
            inpvalue[j + 1] = inpvalue[j]
            j = j - 1
        inpvalue[j + 1] = temp

def bin_sort(inpvalue):
    largest = max(inpvalue)
    length = len(inpvalue)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(inpvalue[i]/size)
        
        if j != length:
            buckets[j].append(inpvalue[i])
        else:
            buckets[length - 1].append(inpvalue[i])
 
    for i in range(length):
        insertion(buckets[i])
 
    res = []
    
    for i in range(length):
        res = res + buckets[i]
 
    return res
 
# bin_sort(array)

 
##-11randomized select
def ordenamientoPorSeleccion(unaLista):
    for llenarRanura in range(len(unaLista)-1,0,-1):
        posicionDelMayor=0
        for ubicacion in range(1,llenarRanura+1):
            if unaLista[ubicacion]>unaLista[posicionDelMayor]:
                posicionDelMayor = ubicacion

        temp = unaLista[llenarRanura]
        unaLista[llenarRanura] = unaLista[posicionDelMayor]
        unaLista[posicionDelMayor] = temp
    return unaLista
# ordenamientoPorSeleccion(unaLista)

##-12Stooge
def stoogesort(A, i, j): 
    if i >= j: 
        return
    if A[i]>A[j]: 
        t = A[i] 
        A[i] = A[j] 
        A[j] = t 
    if j-i + 1 > 2: 
        t = (int)((j-i + 1)/3) 
        stoogesort(A, i, (j-t)) 
        stoogesort(A, i + t, (j)) 
        stoogesort(A, i, (j-t))
    return A 
  
def orderMethod(method, array, samples):
    samples = int(samples)
    ## 01
    if 'Insercion' in method:
        return ordenamientoPorInsercion(array[:samples])  
    ## 02
    if 'Shell' in method:
        return ordenamientoDeShell(array[:samples])
    ## 03
    if 'Bubble' in method:
        return ordenamientoBurbuja(array[:samples])  
    ## 04
    if 'Merge' in method:
        return mergeSort(array[:samples], 0, samples - 1)
    ## 05
    if 'QuickSort' in method:
        return quickSort(array[:samples], 0, samples - 1)  
    ## 06
    if 'Bucket' in method:
        if isinstance(array[0], str): 
            return sorted(array[:samples])  
        else:
            return bucket_sort(array[:samples])
    ## 07
    if 'Radix' in method:
        if isinstance(array[0], str): 
            return sorted(array[:samples])  
        else:
            return radixSort(array[:samples])  
    ## 08
    if 'Heap' in method:
        return heapSort(array[:samples])
    ## 09
    if 'Count' in method:
        if isinstance(array[0], str): 
            return sorted(array[:samples])  
        else:
            return radixSort(array[:samples])  
    ## 10
    if 'Bin' in method:
        if isinstance(array[0], str): 
            return sorted(array[:samples])  
        else:
            return bin_sort(array[:samples])
    ## 11
    if 'RandomiseSelection' in method:
        return ordenamientoPorSeleccion(array[:samples])  
    ## 12
    if 'Stooge' in method:
        return stoogesort(array[:samples], 0, samples - 1)   
    ## Bonus
    if 'PythonSort' in method:
        return sorted(array[:samples])


