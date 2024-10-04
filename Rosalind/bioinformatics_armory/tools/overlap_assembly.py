#################################################
# Overlap assembler
# by smlee

######################
# CUSTOM SCRIPT IMPORT
from itertools import permutations

#############################
# PYTHON NATIVE MODULE IMPORT

def find_overlap(a:str, b:str) -> int:
    """Find overlap and return start position

    Args:
        a: candidate a
        b: candidate b
    
    Returns:
        int(overlap start position)
    """
    m_start = a.find(b[:int(len(b)/2)])
    
    if m_start == -1:
        return 0

    if b.startswith(a[m_start:]):
        return len(a) - m_start

def find_maximum_overlap(reads:list) -> (str, str, int):
    """Find maximum overlap and return 
    candidate a, candidate b and position

    Args:
        reads: list of nucleotide sequences
    
    Returns:
        candidate a, candidate b and start position
    """
    
    cand_a, cand_b = None, None
    max_overlap = 0
    
    for a, b in permutations(reads, 2):    
        overlap = find_overlap(a, b)
        if overlap > max_overlap:
            max_overlap = overlap
            cand_a, cand_b = a, b

    return cand_a, cand_b, max_overlap

def assembly(reads:list) -> str:
    """Find overlap and merge short 
    reads

    Args:
        reads: list of nucleotide sequecnes
    
    Returns:
        str(assembly)
    """

    cand_a, cand_b, overlap = find_maximum_overlap(reads)

    while overlap != 0:
        reads.append(cand_a[:len(cand_a)-overlap] + cand_b)
        reads.remove(cand_a)
        reads.remove(cand_b)

        cand_a, cand_b, overlap = find_maximum_overlap(reads)

    return ''.join(reads)