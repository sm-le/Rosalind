def minimizeSkew(text:str) -> (int):
    """Find genome lengths that minimize skew within the genomic string

    Args:
        text: a genome string
    Returns:
        Generator(genomic length)
    """
    pos = dict()
    i = 1
    s = 0
    while i <= len(text):
        m = text[i-1]
        s += -1 if m == "C" else 1 if m == "G" else 0
        pos[i] = s
        i += 1
    # find minimum
    minV = min(pos.values())
    minPos = [k for k,v in pos.items() if v == minV]
    yield from minPos