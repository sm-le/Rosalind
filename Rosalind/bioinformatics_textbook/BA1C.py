def reverseComplement(text:str) -> str:
    """Reverse complement nucleotide string

    Args:
        text: a dna sequence
    Returns:
        str(reverse complemented string)
    """

    nucSet = {"A":"T","T":"A",
              "G":"C","C":"G",
              "N":"N"}
    
    return ''.join(list(map(lambda x: nucSet[x], list(text[::-1]))))