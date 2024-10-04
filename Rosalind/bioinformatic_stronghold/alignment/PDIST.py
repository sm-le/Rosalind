# Rosalind: Alignment, Phylogeny
# Creating a Distance Matrix

# Question
"""
Given a collection of n (n<=10) DNA strings of equal length.
Return the matrix corresponding to the p-distance d_{p} on the given strngs.

p_distance: the proportion of corresponding symbols that differ between s1 and s2.
"""

from ..tools.fasta_reader import FastaFile
from ..tools.distance import DistanceCalculator
import numpy as np

def CreateDistance(file_name:str):
    """Create Distance among given sequences

    Args:
        file_name: a fasta file path
    Returns:
        np matrix of p-distances
    """
    # Read and save sequence
    sequences = list()
    count = 0
    for record in FastaFile(file_name).collect():
        sequences.append(record.get("sequence"))
        count += 1
    # Empty matrix generation
    mat = np.zeros([count,count],dtype=float)
    for i in range(count):
        for j in range(i+1, count):
            d = DistanceCalculator.p_distance(sequences[i],sequences[j])
            mat[i][j] = d

    # Fill the lower half
    mat = mat + mat.T
    return mat


