"""
# complementing a strand of dna

Given DNA(s), return number of strings that matches its reverse complement.

Example,
IN: 
    >Seq1
    ATAT
OUT: 
    1
"""

from tools.fasta import Fasta
from tools.reverse_complement import rcomplement_dna

def complement_check(file:str) -> int:
    """check sequence and count if complement yield the same

    Args:
        file: file
    Returns:
        int(same string result count)
    """

    c = 0
    for record in Fasta.parse(file):
        if rcomplement_dna(record.seq) == record.seq:
            c += 1

    return c