import random


def fillArray(A, n):

    for i in range(1, n):
        A[i]=random.randint(1, 10)
    return A

#Ordenar el arreglo A[n]
def sortArray(A, n):
    for i in range(1, n):
        for j in range(i, n):
            if(A[i] > A[j]):
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A


#Algoritmo de busqueda binaria
def algoritmo(A, low, high, v):
    if (low <= high):
        mid = (low + high) // 2
        print("mid", mid, "\n")
        if (A[mid] == v):
            return mid  # Element found
        elif (A[mid] < v):
            print("The element is in the right side\n")
            return algoritmo(A, mid + 1, high, v)
        else:
            print("The element is in the left side\n")
            return algoritmo(A, low, mid-1, v)
    return -1  # Element not found

def main():
    size = 8
    A = [0]*size
    fillArray(A, size)
    sortArray(A, size)
    print("Sorted Array:", A)
    v = 4
   
    result = algoritmo(A, 0, size -1, v)
    if result != -1:
        print(v, "found at index:", result)
    else:
        print(v, "not found in the array.")

main()


    
