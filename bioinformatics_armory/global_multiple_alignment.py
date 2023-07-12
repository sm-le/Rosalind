"""
# Global multiple alignment
## used mafft instead of clustalw2 since the program had officially retired.

Given a set of nucleotide strings, return id of the most different string. 

Example,
IN: 
    >Rosalind_18
    GACATGTTTGTTTGCCTTAAACTCGTGGCGGCCTAGCCGTAAGTTAAG
    >Rosalind_23
    ACTCATGTTTGTTTGCCTTAAACTCTTGGCGGCTTAGCCGTAACTTAAG
    >Rosalind_51
    TCCTATGTTTGTTTGCCTCAAACTCTTGGCGGCCTAGCCGTAAGGTAAG
    >Rosalind_7
    CACGTCTGTTCGCCTAAAACTTTGATTGCCGGCCTACGCTAGTTAGTTA
    >Rosalind_28
    GGGGTCATGGCTGTTTGCCTTAAACCCTTGGCGGCCTAGCCGTAATGTTT

OUT:
    Rosalind_7
"""

from tools.mafft import mafft
from tools.fasta import Fasta

def get_most_divergent(file:str) -> str:
    """Get the most different record from a series of sequences

    Args:
        file: a fasta file
    Returns:
        str(most different record id)
    """
    
    outp = mafft(file, f"{''.join(file.split('/')[-1])}/rst.txt")

    id = None
    gap_count = 1e9
    for record in Fasta.parse(outp):
        if record.seq.count("-") < gap_count:
            id = record.id
            gap_count = record.seq.count("-")

    return id

