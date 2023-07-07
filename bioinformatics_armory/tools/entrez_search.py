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

def entrez_search(organism:str, start_date:str, end_date:str):
    """search genbank record  
    from biopython entrez api 

    Args:
        organism: scientific name of the organism
        start_date: initial publication date
        end_date: end publication date
    
    Returns:
        int(number of records)
    """

    Entrez.email = "(intentionally-left-blank)@seegene.com"
    handle = Entrez.esearch(db="nucleotide", term=f'"{organism}"[Organism] AND ("{start_date}"[Publication Date]:"{end_date}"[Publication Date])')
    record = Entrez.read(handle)
    handle.close()

    return record