def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """

    if len(array) == 0:
        return 0
    else:
        return sum((array[::2])*array[-1])

        
print checkio([0, 1, 2, 3, 4, 5])
print checkio([1, 3, 5])
print checkio([6])
print checkio([])
