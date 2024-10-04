"""
A string u is a common subsequence of s and t if the symbol u appears in order as a subsequence of both s and t.

Q: Given two DNA string s and t, return a longest common subsequence.
"""

from Bio import SeqIO
import numpy as np

def findSharedSplicedMotif(fasta_path:str) -> str:
    """Find a Shared Spliced Motif between two sequences

    Args:
        fasta_path: path to a fasta file
    Returns:
        str(shared motif)
    """
    # load data
    seqs = list()
    for record in SeqIO.parse(fasta_path,"fasta"):
        seqs.append(record.seq)
    
    s1 = seqs[0]
    s2 = seqs[1]

    # matrix initialization
    mat = np.zeros((len(s1)+1, len(s2)+1))

    # matrix fillup
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            mat[i][j] = mat[i-1][j-1] + 1 if s1[i-1] == s2[j-1] \
            else max(mat[i][j-1], mat[i-1][j])

    # traceback
    i,j = len(s1), len(s2)
    motif = str()

    while mat[i,j] > 0:
        if mat[i][j-1] == mat[i][j]:
            j -= 1
        elif mat[i-1][j] == mat[i][j]:
            i -= 1
        else:
            motif += s1[i-1] # alt s2[j-1]
            i -= 1
            j -= 1
    
    return motif[::-1]