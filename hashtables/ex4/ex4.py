def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    neg = [ i for i in a if i < 0]

    for i in neg:
        if a.count(-i) > 0:
            result.append(-i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

    a = list(range(5000000))
    a += [-1,-2,-3]

    has_negatives(a)
