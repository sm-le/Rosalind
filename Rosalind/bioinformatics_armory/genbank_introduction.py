"""
# Armory 2

Given a genus name and two dates, return the number of genbank entries

Example,
IN: 
    Anthoxanthum
    2003/7/25
    2005/12/27
OUT: 7
"""

import tools.entrez_search as es

def record_count(file:str) -> int:
    """
    Search genbank and return number of record in integer format

    Args:
        file: a name of a file
    
    Returns:
        len(number of records)
    """

    with open(file,"r") as f:
        name = next(f).strip()
        start = next(f).strip()
        end = next(f).strip()
    
    record = es.entrez_search(name, start, end)

    return int(record["Count"])