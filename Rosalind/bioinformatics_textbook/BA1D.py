def findPattern(text:str, pattern:str) -> (int):
    """Find all pattern occurrences within the given string/text

    Args:
        text: a target
        pattern: a query
    Returns:
        Generator(all positions)
    """
    fposList = list()
    spos = 0
    while True:
        m = text[spos:].find(pattern)
        if m != -1:
            fposList.append(m+spos)
            spos += m + 1
        else:
            break
    
    for pos in fposList:
        yield pos