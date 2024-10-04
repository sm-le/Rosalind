#################################################
# Reverse complement
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT

def rcomplement_dna(sequence:str) -> str:
    """Complement given dna sequence to reverse
    strand

    Args:
        sequence: a nucleotide sequence

    Returns:
        string("TGCA....")
    """

    complement_table = {
                        "A":"T",
                        "T":"A",
                        "C":"G",
                        "G":"C"
                    }
    
    sequence = "".join([complement_table[x] for x in  sequence[::-1]])

    return sequence