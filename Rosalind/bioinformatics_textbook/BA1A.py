def countPattern(text:str, pattern:str) -> int:
    """Find the pattern in the text and return a total number of matches

    Args:
        text: a target text
        pattern: a pattern to find
    Returns:
        int(match count)
    """
    cur = 0
    pos = list()
    while True:
        try:
            m = text[cur:].index(pattern)
            pos.append(m+cur)
            cur += (m + 1)
        except:
            break

    return pos