from itertools import product
def patternNumber(text:str) -> int:
    """Convert pattern to number

    Args:
        text: a target string
    Returns:
        int(pattern number)
    """
    n = {"A":0,"C":1,"G":2,"T":3}
    number = 0
    for i, nuc in enumerate(text):
        number += n.get(nuc) * (4 ** (len(text)-1-i))
    return number
