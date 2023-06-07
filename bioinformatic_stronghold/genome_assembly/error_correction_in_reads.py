import sys
sys.path.append("/home/smlee/repo/Rosalind/bioinformatic_stronghold/")

from alignment.counting_point_mutation import hamming_distance_v1
from string_algorithm.complementing_a_strand_of_dna import rcomplement_dna_v2
from tools.fasta_reader import FastaFile

"""
# genome assembly 2

Given a collection of equal length sequences, return a list of all corrections in the format of old_read->new_read

Example,
IN: 
    >Rosalind_52
    TCATC
    >Rosalind_44
    TTCAT
    >Rosalind_68
    TCATC
    >Rosalind_28
    TGAAA
    >Rosalind_95
    GAGGA
    >Rosalind_66
    TTTCA
    >Rosalind_33
    ATCAA
    >Rosalind_21
    TTGAT
    >Rosalind_18
    TTTCC
OUT:
    TTCAT->TTGAT
    GAGGA->GATGA
    TTTCC->TTTCA
"""

def error_correction(path:str):
    """Correct sequencing error with 1 hamming distance 
    and print corrected read

    Args:
        path: path to read file
    """
    # make count library
    sequence_count = dict()
    with FastaFile(path) as fa:
        for record in fa.body:
            try:
                if rcomplement_dna_v2(record['sequence']) in sequence_count:
                    sequence_count[rcomplement_dna_v2(record['sequence'])] += 1
                else:
                    sequence_count[record['sequence']] += 1
            except:
                sequence_count[record['sequence']] = 1

    # clean up 
    errors = dict(filter(lambda x: x[1] == 1, sequence_count.items()))
    for error in errors:
        del sequence_count[error]

    # correct reads
    for error in errors:
        for read in sequence_count:
            dist = hamming_distance_v1(error,read)
            if dist == 1:
                print(f"{error}->{read}")
            else:
                rdist = hamming_distance_v1(error,rcomplement_dna_v2(read))
                if rdist == 1:
                    print(f"{error}->{rcomplement_dna_v2(read)}")