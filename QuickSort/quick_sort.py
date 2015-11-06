coms = 0

def add_coms(amount):
    global coms
    coms += amount

def quicksort(array):
    # add_coms(len(array))
    if len(array) > 1:
        pivot = array[0]
        print("Array Before: {0}, pivot: {1}".format(array, pivot))
        i = 1
        for elem in array[1:]:
            if elem < pivot:
                array[array.index(elem)], array[i] = array[i], array[array.index(elem)]
                i+=1
                # print(array)
        array[i-1], array[0] = array[0], array[i-1]
        # print("Array After: {0}, i: {1}".format(array, i))
        quicksort(array[:i-1])
        # print("Array After Left Sort: {0}".format(array))
        quicksort(array[i:])
        # print("Array After Right Sort: {0}".format(array))
        array[:] = quicksort(array[:i-1]) + [pivot] + quicksort(array[i:])
    return array

def main():
    f = open('QuickSort.txt')
    my_array = [int(line) for line in f.readlines()]
    # my_array = [5, 8, 2, 3, 1, 4, 7, 6]
    quicksort(my_array)
    print(my_array)
    print(coms - len(my_array))

if __name__ == "__main__":
    main()
