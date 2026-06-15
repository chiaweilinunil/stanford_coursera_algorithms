FILE_PATH = 'm1w3.txt'


def main():
    with open(FILE_PATH) as f:
        arr = [int(line) for line in f]
    answer=QuickSort(arr, 0, len(arr) - 1)
    print(answer)
    # TODO: print the total comparison count

def QuickSort(array, l, r):
    if l >= r:
        return 0
    counter = (r - l) 
    p = Partition(array, l, r)
    counter += QuickSort(array, l, p-1)
    counter += QuickSort(array, p + 1, r)
    return counter
    

def Partition(array, l, r):
    array[l], array[r] = array[r], array[l]
    pivot = array[l]
    i = l + 1
    for j in range(l+1, r+1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[l], array[i - 1] = array[i - 1], array[l]   
    return i - 1    


if __name__ == "__main__":
    main()
