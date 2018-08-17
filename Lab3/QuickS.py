def QuickSort(array,p,r):
    if p < r:
        q = Partition(array, p,r)
        QuickSort(array, p, q-1)
        QuickSort(array,q+1,r)

def Partition(array, p, r):
    i = (p - 1)  # indice del elemento mas pequeño
    pivot = array[r]  # pivot

    for j in range(p, r):

        #Si el elemento actual es menor o igual al pivot
        if array[j] <= pivot:
            #Incrementa el indice del elemento menor
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[r] = array[r], array[i + 1]
    return (i + 1)





unsorted_array = [5, 10, 15, 32, 55, 21, 40, 2, 3, 76, 89, 28, 9, 7]

QuickSort(unsorted_array, 0, len(unsorted_array) - 1)
print unsorted_array
