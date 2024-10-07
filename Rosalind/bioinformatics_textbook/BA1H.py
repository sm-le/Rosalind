from BA1G import hamming
def apprxPatternFinder(text:str,
                       pattern:str,
                       mismatch:int) -> (int):
    """Find patttern within a text with maximum allowed mismatches

    Args:
        text: target text
        pattern: pattern to find
        mismatch: allowed number of mismatches
    Returns:
        generator(positional index)
    """
    pos = list()
    for i in range(len(text) - len(pattern) + 1):
        subject = text[i:i+len(pattern)]
        d = hamming(subject,pattern)
        if d <= mismatch:
            pos.append(i)
    
    yield from pos