"""
# finding genes with orfs

Given a dna, return the longest protein translated.

Example,
IN: 
   AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
OUT:
   MLLGSFRLIPKETLIQVAGSSPCNLS
"""

from tools.translation import translate
from tools.reverse_complement import rcomplement_dna

def get_orf_ss(dna:str):
    """Take a strand of dna and translate
    
    Args:
        dna: dna sequence

    Returns:
        list(proteins)
    """
    # check orf
    ## products
    proteins = list()
    ## consider frame shift
    for frame in range(0,3):
        protein = ''
        tr = False

        for idx in range(frame, len(dna)-3, 3):
            if dna[idx:idx+3] == 'ATG':
                tr = True
            if tr:
                aa = translate(dna[idx:idx+3])

                if aa == "*":
                    proteins.append(protein)
                    tr, protein = False, ''
                
                else:
                    protein += aa

    return proteins

def longest_orf(file:str) -> str:
    """Get longest protein seq

    Args:
        file: file containing a strand of dna
    Returns:
        str(protein)
    """
    # get dna materials
    with open(file,"r") as f:
        dna = next(f).strip()

    rdna = rcomplement_dna(dna)

    # products
    proteins = list()

    # get orfs
    proteins.extend(get_orf_ss(dna))
    proteins.extend(get_orf_ss(rdna))

    return max(proteins, key=len)