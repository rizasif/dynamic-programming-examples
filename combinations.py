def sum_to_n(n, size, limit=None):
    " Produce all lists of `size` positive integers in decreasing order "
    " that add up to 'n' "

    # If number is same then return itself
    if size == 1:
        yield [n]
        return
    
    # Set an end limit
    if limit is None:
        limit = n
    
    # Start of the number set
    start = (n + size - 1) // size

    # The number set to be stopped at
    stop = min(limit, n - size + 1) + 1

    # Produce recursive results
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail

def possibleCombinations(N):
    "This function produces all possible natural number set which can sum up to a number 'N'"
    
    # For first 10 possible number of solutions
    for i in range(10):
        for partition in sum_to_n(N, i+1):
            # print partition, a python generator for the possible combinations
            pstr = ""
            for i in partition:
                pstr = pstr + str(i) + "+"
            pstr = pstr[:len(pstr)-1]
            print pstr
