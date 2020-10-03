from time import sleep
#===================================
#BUBBLESORT
def bubbleSort(A): 
    for i in range(len(A)):         
        for j in range(0, len(A)-i-1):             
            if A[j] > A[j+1] : 
                A[j], A[j+1] = A[j+1], A[j] 

    return A

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
