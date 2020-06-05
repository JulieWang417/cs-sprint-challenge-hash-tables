

# O(n**2)
def intersection(arrays):
    
    # empty dict
    int_counts = {}
    # arrays here is a array of array
    for arr in arrays:
        # in case there are multiple same number in a arr
        for x in set(arr):
            # if x is not found, initial key x to value = 0, x:0
            if x not in int_counts:
                int_counts[x] = 0
            # if x exists, add 1 to x's value
            int_counts[x] += 1

    # empty list
    result = []
    # loop all key, value
    for key,value in int_counts.items():
        # value is the number that presents the total times we found it in arrays
        # if value equals the length of the array, we would say that the number exist in all lists
        if value == len(arrays):
            # append the number
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))

