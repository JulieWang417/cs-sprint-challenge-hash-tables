def get_indices_of_item_weights(weights, length, limit):
    length = len(weights)
    # set up a hash table, here we store each weight as keys
    weight_index = {k:v for k,v in zip(weights, range(0,length))} 
    # The zip() function takes iterables, aggregates them in a tuple, and return it.
    # if weights=[9,6,3,15,24]
    # wight_index = {9: 0, 6: 1, 3: 2, 15: 3, 24: 4}
    # print(weight_index)

    for index in range(0,length):
        # Get current weight
        current_weight = weights[index]
        # Calculate target weight to reach limit 
        target_weight = limit - current_weight
        # If that weight is in the weight_index
        if target_weight in weight_index:
            # if current_weight is greater than target_weight
            if index > weight_index[target_weight]:
                return (index, weight_index[target_weight])
            else:
                return (weight_index[target_weight], index)

    return None
"""
weights = [9,6,3,15,24]
limit = 21
length = len(weights)
print(get_indices_of_item_weights(weights, length, limit))


h = {1:"a",2:"b",3:"c"}
def a(i):
    if i in h:
        print("True")
    else:
        print("False")

a("c")
"""