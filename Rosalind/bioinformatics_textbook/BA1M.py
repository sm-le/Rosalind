def numberPattern(idx:int,
                  k:int) -> int:
    """Convert pattern to number

    Args:
        idx: pattern index
        k: kmer size
    Returns:
        str(pattern)
    """
    n = {0:"A",1:"C",2:"G",3:"T"}
    pat = ""
    for _ in range(k):
        r = idx % 4
        pat += n.get(r)
        idx //= 4
    
    return pat[::-1]