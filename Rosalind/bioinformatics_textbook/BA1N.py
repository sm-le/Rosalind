from BA1G import hamming
from itertools import product
def neigborString(text:str,
                  d:int) -> (str):
    """Generate neighbor strings with d distance

    Args:
        text: a target text
        d: hamming distance
    Returns:
        generator(neighbors with d distance)
    """
    n = {'A','C','T','G'}
    ngbr = (''.join(i) for i in product(n,repeat=len(text)) if hamming(''.join(i),text) <= d)
    yield from ngbr