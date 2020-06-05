"""
def has_negatives(arr):

    neg = {k:k*-1 for k in arr}
    result = []
    for k in neg:
        if neg[k] in neg:
            if k > 0:
                result.append(k)
"""
# above codes work, below is another way using set object
# O(n)
def has_negatives(arr):

    # use set object to store all the negative numbers, {-1,-2,-4}
    values = set([n for n in arr if n<0])
    
    result = []
    for k in arr:
        # append, if k > 0 and have corresponding negative numbers in the set
        if k > 0 and (-k in values):
            result.append(k)

    return result

if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))