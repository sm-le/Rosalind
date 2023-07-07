"""
# Armory 1

Given a DNA string of length 1000 bp, return counts of A, C, G, and T separated by \s

Example,
IN: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
OUT: 20 12 17 21
"""

def count_ACGT_v2(sequence:str) -> str:
    """Count ACGT individually given input 
    nucleotide sequence

    Args:
        sequence: a nucleotide sequence

    Returns:
        string(count(A)\scount(C)\scount(G)\scount(T))
    """

    # Loop dictionary
    nuc_count = dict()
    for nuc in sequence:
        try:
            nuc_count[nuc] += 1
        except:
            nuc_count[nuc] = 1

    return f"{nuc_count['A']} {nuc_count['C']} {nuc_count['G']} {nuc_count['T']}"