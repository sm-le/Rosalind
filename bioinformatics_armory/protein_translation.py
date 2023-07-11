"""
# protein translation

Given a DNA string, and a protein string, return genetic code variant for translation.

Example,
IN: 
    ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
    MAMAPRTEINSTRING
OUT:
    1
"""

from tools.translation import translate

def get_table_info(file:str) -> int:
    """Get translation table information

    Args:
        file: file with DNA and protein strings
    Returns:
        int(code table index)
    """

    with open(file,"r") as f:
        dna = next(f).strip()
        protein = next(f).strip()

    index_to_try = 1
    while True:
        try:
            cand_protein = translate(dna, str(index_to_try)).strip("*")

            if cand_protein == protein or index_to_try > 15:
                break
                
            index_to_try += 1
        except:
            index_to_try += 1

    return index_to_try