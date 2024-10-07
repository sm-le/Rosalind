def hamming(s1:str,
            s2:str) -> int:
    """Calculate hamming distance between two strings

    Args:
        s1: target string
        s2: query string
    Returns:
        int(hamming distance)
    """
    
    m = [a==b for a,b in zip(s1,s2)]
     
    return m.count(False)