#################################################
# Download ncbi record from NCBI
# by smlee

######################
# CUSTOM SCRIPT IMPORT

#############################
# PYTHON NATIVE MODULE IMPORT

from Bio import Entrez

######
# MAIN

def entrez_fetch(accession):
    """Download ncbi sequence  
    from biopython entrez api
    """

    Entrez.email = "(intentionally-left-blank)@seegene.com"
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text")
    record = handle.readlines()
    # record = "".join(map(lambda x: x.strip(), record[:]))

    handle.close()

    return record