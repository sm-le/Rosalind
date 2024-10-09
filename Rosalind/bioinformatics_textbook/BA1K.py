from itertools import product
def frequencyArray(text:str,k:int) -> (int):
    """Generate frequency array given string and k size

    Args:
        text: target text
        k: kmer size
    Returns:
        frequency in generator
    """
    n = ['A','C','G','T']
    fdict = {''.join(i):0 for i in product(n,repeat=k)}
    for i in range(len(text)-k+1):
        fdict[text[i:i+k]] += 1
    yield from fdict.values()