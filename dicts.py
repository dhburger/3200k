
def hist(s):
    """returns the histogram of the characters in s

    >>> hist("AAGGT")
    {'A': 2, 'T': 1, 'G': 2}

    >>> hist("!!xx")
    {'!': 2, 'x': 2}

    """
    results = {}
    for l in s:
        if l not in results:
            results[l] = 1
        else:
            results[l] += 1 
    return results


def str_to_int(s):
    """converts a string to an integer value

    >>> str_to_int('s')
    115

    >>> str_to_int('st!ll')
    11511633108108L

    hint: the built in ord and chr functions
    """
    results = []
    for symbol in s:
        results.append(str(ord(symbol)))
    return int("".join(results))
    


def null_list(length):
    """return a list of all None values of given length

    >>> null_list(3)
    [None, None, None]

    >>> null_list(1)
    [None]

    """
    results = []
    for something in range(length):
        results.append(None)
    return results
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
