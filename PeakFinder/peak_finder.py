def find_peak(array, left = None, right = None):
    # print("Finding peak in:{0}".format(array))
    n = len(array)
    if n < 1:
        return False
    if n == 1:
        return array[0]
    if n == 2:
        if left:
            if array[0] >= array[1]:
                return array[0]
            else:
                return False
        elif right:
            if array[1] >= array[0]:
                return array[1]
            else:
                return False
        if array[0] >= array[1]:
            return array[0]
        else:
            return False
        if array[1] >= array[0]:
            return array[1]
        else:
            return False
    middle = n // 2

    if array[middle] >= array[middle - 1] and array[middle] >= array[middle+1]:
        return array[middle]
    else:
        peak_left = find_peak(array[:middle], left=True)
        peak_right = find_peak(array[middle:], right=True)
        if peak_left >= peak_right:
            return peak_left
        if peak_right >= peak_left:
            return peak_right
        # print("Found no peak at all.")
        peak = False
        return peak


if __name__=="__main__":
    import profile

    arrays = {
    5: [1,2,3,4,5],
    6: [6,5,4,3,2,1],
    4: [1,2,3,4,3,2,1],
    3: [1,3,2,2,3,1],
    3: [2,2,3,3,3,5,3],
    100000: range(100001)
    }

    for value, array in arrays.items():
        profile.run("print(find_peak(array))")