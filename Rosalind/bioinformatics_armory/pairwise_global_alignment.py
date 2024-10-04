"""
# pairwise global alignment

Given two genbank ids, return maximum alignment score

Example,
IN: 
    JX205496.1 JX469991.1
OUT:
    257
"""

from tools.entrez_fetch import entrez_fetch
from tools.needle import needle

def pairwise_alignment_with_needle(ifile:str, query:str, subject:str, outpath:str) -> str:
    """Get sequence from genbank accession and run pairwise alignment with needle

    Args:
        ifile: input accession file
        query: query sequence file
        subject: subject sequence file
        outpath: needle output path

    Returns:
        str(needle output path)
    """
    # prepare analysis file
    afiles = iter([query,subject])

    with open(ifile, "r") as f:
        accessions = next(f).split()

    for accession in accessions:
        entry = entrez_fetch(accession)
        hdr = entry[0]
        seq = ''.join(entry[1:])

        with open(next(afiles), "w") as f:
            f.write(hdr)
            f.write(seq)
    
    # run needle
    o = needle(query, subject, outpath)

    return o