import random
def fillArray(A, n):

    for i in range(1, n):
        A[i]=random.randint(1, 10)
    return A

#pero no entiendo o sea mi pseudocodigo seria algo asi:


#def algoritmo(array):
   #if len(array) == 1:
    #    return array, 0
    #else: 
        
def sortArray(A, n):
    for i in range(1, n):
        for j in range(i, n):
            if(A[i] > A[j]):
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A


def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a= arr[:len(arr)//2]
        b= arr[len(arr)//2:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
        while(i< len(a) and j < len(b)):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1

             





#  [0, 10, 6, 3, 2, 10, 3, 6]
#
 # [0, 10, 6, 3]


  #[2, 10, 3, 6]

 

def main():
    A =[3, 7, 10, 14, 18, 19, 2, 11, 16, 17, 23, 25]
    print("Array:", A)


    print(mergeSortInversions(A))

    
main()