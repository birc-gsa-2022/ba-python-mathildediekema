"""Module for computing border arrays."""
import numpy as np

def border_array(x):

    if x == '':
        return []

    ba = np.zeros(len(x), dtype = int)
    ba[0] = 0
    for i in range(1,len(x)):
        b = ba[i - 1]
        while b > 0 and x[i] != x[b]:
            b = ba[b - 1]
        if x[i] == x[b]:
            ba[i] = b + 1
        else:
            ba[i] = 0

    return ba
    """
    Construct the border array for x.

    >>> border_array("aaba")
    [0, 1, 0, 1]
    >>> border_array("ississippi")
    [0, 0, 0, 1, 2, 3, 4, 0, 0, 1]
    >>> border_array("")
    []
    """



def strict_border_array(x):

    ba = border_array(x)
    for i in range(len(x) - 1):
        if ba[i] > 0 and x[ba[i]] == x[i + 1]:
            ba[i] = ba[ba[i] - 1]
    return ba


    """
    Construct the strict border array for x.

    A strict border array is one where the border cannot
    match on the next character. If b is the length of the
    longest border for x[:i+1], it means x[:b] == x[i-b:i+1],
    but for a strict border, it must be the longest border
    such that x[b] != x[i+1].

    >>> strict_border_array("aaba")
    [0, 1, 0, 1]
    >>> strict_border_array("aaaba")
    [0, 0, 2, 0, 1]
    >>> strict_border_array("ississippi")
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 1]
    >>> strict_border_array("")
    []
    """
   

