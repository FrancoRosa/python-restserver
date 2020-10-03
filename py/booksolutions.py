from time import sleep
#=================================
#INSERT
def insertionSort(A): 
    for j in range(1, len(A)):
        key = A[j] 
        i = j-1
        while i >= 0 and A[i] > key : 
            A[i + 1] = A[i] 
            i = i - 1
        A[i+1] = key 
    return A  

#================================
#SHELLSORT

def shellSort(A): 
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

A = [ 12, 34, 54, 2, 3] 
A = [ 'A','Z','X','C',] 
print(A)
print(shellSort(A)) 


#===================================
#BUBBLESORT
def bubbleSort(A): 
    for i in range(len(A)):         
        for j in range(0, len(A)-i-1):             
            if A[j] > A[j+1] : 
                A[j], A[j+1] = A[j+1], A[j] 

    return A


#======================================
#MERGE

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


#===================================
#QUICKSORT
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




#==================================0
#HEAP

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

A = [ 12, 11, 13, 5, 6, 7] 
print(A)
print(heapSort(A)) 

#=================================
#STOOGESORT

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
     
A = [20,8,5,21,55,8] 
n = len(A) 

print(A)  
print(stoogesort(A, 0, n-1)) 
   

A = [2, 3, 5, 1, 5, 9, 7, 2, 8]
print(A) 
print(mergeSort(A, 0, len(A) - 1))


A = [4, 1, 11, 13, 5, 6] 
A = ['z','a','e','i','vi','x','a']
print(A)
print(insertionSort(A)) 

A = [64, 34, 25, 12, 22, 11, 90,1] 
A = ['z','a','e','i','vi','x','a']
print(A)  
print(bubbleSort(A)) 

A = [10, 7, 8, 9, 1, 5,12]
A = ['z','a','e','i','v','xi','a']
print(A)
print(quickSort(A, 0, len(A)-1))