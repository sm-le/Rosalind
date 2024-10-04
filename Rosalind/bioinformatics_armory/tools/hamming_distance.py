#################################################
# Hamming distance
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT

def hamming_distance_v1(sequence_1:str, sequence_2:str) -> int:
    """Calculate hamming distance between 
    two DNA sequences and return hamming distance 
    aka difference between two string in 
    nucleotide level

    Args:
        sequence_1: first nucleotide sequence
        sequence_2: second nucleotide sequence

    Returns:
        The hamming distance in numeric form
    """

    hamming_distance = sum([i!=j for i, j in zip(list(sequence_1), list(sequence_2))])

    return hamming_distance