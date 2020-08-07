def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    dictionary = dict()

    for i in range(length):
        dictionary.update({weights[i]: i})

    for key, value in dictionary.items():
        x = limit - key
        if x in dictionary:
            if dictionary.get(x) is value:
                return(value, dictionary.get(x) - 1)
            else:
                if dictionary.get(x) > value:
                    return (dictionary.get(x), value)
                else:
                    return (value, dictionary.get(x))

    return None