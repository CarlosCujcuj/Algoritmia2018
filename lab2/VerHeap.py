def MayHeap(array):
    leng = len(array)
    verf = 0 #es el indice del right child
    i = 1 #indice del array
    h = 'y' #si es heap o no

    while verf < leng and h == 'y': #verifica si su child esta dentro del length del array y si
        verf = 2*i                  # al momento todavia es heap ('y')
        if array[i-1] < array[verf-1]:
            h = 'n'

        if verf < leng:
            if array[i-1] < array[verf]:
                h = 'n'

        i += 1

    if h == 'y':
        print 'Es Heap'
    else:
        print 'No es Heap'



possible_heap = [16,14,10,8,7,9,3,2,4,1]
MayHeap(possible_heap)