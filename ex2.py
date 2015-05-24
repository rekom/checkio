def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if len(array) < n :
        return -1
    elif len (array) >= n:
        n = array[n]**n
        return n
    else:
        return None


print index_power([1, 2, 3, 4], 2)
print index_power([1, 3, 10, 100], 3)
print index_power([0, 1], 0)
print index_power([1, 2], 3)
