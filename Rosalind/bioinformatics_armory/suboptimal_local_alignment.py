"""
# Suboptimal local alignment

Given two DNA strings s and t, there are inexact repeat r of 32-40 bp. Return the total number of 
occurrences of r as a substring of s and t respectively.

Example,
IN: 
    >Rosalind_12
    GACTCCTTTGTTTGCCTTAAATAGATACATATTTACTCTTGACTCTTTTGTTGGCCTTAAATAGATACATATTTGTGCGACTCCACGAGTGATTCGTA
    >Rosalind_37
    ATGGACTCCTTTGTTTGCCTTAAATAGATACATATTCAACAAGTGTGCACTTAGCCTTGCCGACTCCTTTGTTTGCCTTAAATAGATACATATTTG
OUT:
    2 2
"""

from tools.lalign import lalign
from tools.fasta import Fasta
from tools.hamming_distance import hamming_distance_v1 as hd

def count_repeats(file:str) -> int:
    """count repeat element within a string

    Args:
        file: rosalind input fasta
    Returns:
        str(repeat_in_a\srepeat_in_b)
    """

    # set path
    base_path = '/'.join(file.split("/")[:-1])
    f = ['a','b']
    temp_f = iter(f)

    # write separate fasta file
    for record in Fasta.parse(file):
        with open(f"{base_path}/{next(temp_f)}.txt","w"):
            f.write(f">{record.id}\n{record.seq}\n")
    
    # run lalign
    p = lalign(f"{base_path}/{f[0]}.txt", f"{base_path}/{f[1]}.txt", f"{base_path}/rst.txt")

    # get repeat
    with open(p) as f:
        for line in f:
            if "100.0%" in line:
                next(f)
                next(f)
                repeat = next(f).split()[-1].strip()
                break

    # find repeat count
    count = str()
    for record in Fasta.parse(file):
        d = 0
        for i in range(len(record.seq)-len(repeat)):
            dist = hd(repeat, record.seq[i:i+len(repeat)])
            if dist <= 3:
                d += 1
        
        count += f"{d}\s"

    return count.strip()