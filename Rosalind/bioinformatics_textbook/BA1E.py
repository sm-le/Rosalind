from collections import defaultdict
def clumpFinder(text:str,
                L:int,
                t:int,
                k:int) -> (str):
    """Find k-length clump occuring t times within L range of a genome (text)

    Args:
        text: a target string
        L: length boundary
        t: minimum occurrence
        k: k-mer size
    Returns:
        generator(clumps)
    """
    Clumps = set()
    iClump = defaultdict(int)
    for i in range(len(text)-L+1):
        subText = text[i:i+L]
        if len(subText) < L:
            break
        for j in range(len(subText)-k+1):
            iClump[subText[j:j+k]] += 1
        Clumps.update(dict((k,v) for k,v in iClump.items() if v >= t).keys())
        iClump = defaultdict(int)
        
    yield from Clumps
