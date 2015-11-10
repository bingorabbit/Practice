"""
A simple script to count array inversions.
"""
__author__ = 'bingorabbit'


def count_split_inversion(a, left_half, right_half):
    sum = 0
    sorted_list = []
    i, k = 0, 0
    while i < len(left_half) and k < len(right_half):
        if left_half[i] < right_half[k]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[k])
            sum += len(left_half) - i
            k += 1
    # print("Sorted List Mid Merge: {0}".format(sorted_list))
    while i < len(left_half):
        sorted_list.append(left_half[i])
        i += 1

    while k < len(right_half):
        sorted_list.append(right_half[k])
        k += 1
    return sorted_list, sum


def count_inversions(a):
    # Bad solution as running time: O(n^2)
    # x,y, sum = 0,0,0
    # for x in a:
    #     for y in a[a.index(x)+1:]:
    #         if x > y:
    #             sum +=1
    # return sum

    if len(a) <= 1:
        return a, 0
    else:
        mid = len(a) // 2
        if len(a) == 2:
            if a[0] > a[1]:
                return [a[1], a[0]], 1
        left_half, x = count_inversions(a[:mid])  # => 0
        right_half, y = count_inversions(a[mid:])  # => 1
        sorted_list, z = count_split_inversion(a, left_half, right_half)
        return sorted_list, x + y + z


def main():
    f = open('IntegerArray.txt')
    my_array = [int(line) for line in f.readlines()]
    print(count_inversions(my_array)[1])


if __name__ == "__main__":
    main()
