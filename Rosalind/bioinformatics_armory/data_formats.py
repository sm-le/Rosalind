"""
# Armory 3

Given a collection of genbank entries, return shortest of strings in fasta format

Example,
IN: 
    JX469983 AB028831
OUT: 
    >JX469983.1 Zea mays subsp. mays clone UT3343 G2-like transcription factor mRNA, partial cds
    ATGATGTATCATGCGAAGAATTTTTCTGTGCCCTTTGCTCCGCAGAGGGCACAGGATAATGAGCATGCAA
    GTAATATTGGAGGTATTGGTGGACCCAACATAAGCAACCCTGCTAATCCTGTAGGAAGTGGGAAACAACG
    GCTACGGTGGACATCGGATCTTCATAATCGCTTTGTGGATGCCATCGCCCAGCTTGGTGGACCAGACAGA
    GCTACACCTAAAGGGGTTCTCACTGTGATGGGTGTACCAGGGATCACAATTTATCATGTGAAGAGCCATC
    TGCAGAAGTATCGCCTTGCAAAGTATATACCCGACTCTCCTGCTGAAGGTTCCAAGGACGAAAAGAAAGA
    TTCGAGTGATTCCCTCTCGAACACGGATTCGGCACCAGGATTGCAAATCAATGAGGCACTAAAGATGCAA
    ATGGAGGTTCAGAAGCGACTACATGAGCAACTCGAGGTTCAAAGACAACTGCAACTAAGAATTGAAGCAC
    AAGGAAGATACTTGCAGATGATCATTGAGGAGCAACAAAAGCTTGGTGGATCAATTAAGGCTTCTGAGGA
    TCAGAAGCTTTCTGATTCACCTCCAAGCTTAGATGACTACCCAGAGAGCATGCAACCTTCTCCCAAGAAA
    CCAAGGATAGACGCATTATCACCAGATTCAGAGCGCGATACAACACAACCTGAATTCGAATCCCATTTGA
    TCGGTCCGTGGGATCACGGCATTGCATTCCCAGTGGAGGAGTTCAAAGCAGGCCCTGCTATGAGCAAGTC
    A
"""

from Bio import Entrez
import tools.entrez_fetch as ef



def shortest_entry(path:str, file:str):
    """Get genbank entries from a file and return a shortest entry in fasta file

    Args:
        path: path to a file with entries
        file: save file path
    """

    with open(path) as f:
        entries = next(f).split()


    seq_d = dict()
    llen = None
    lid = None
    with open(file) as f:
        for acc in entries:
            
            record = ef.entrez_fetch(acc)

            gid = record[0]
            gseq = record[1:]
            lseq = len("".join(map(lambda x: x.strip(), gseq)))

            seq_d[gid] = gseq

            if llen is None and lid is None:
                llen = lseq
                lid = gid
            elif llen > lseq:
                llen = lseq
                lid = gid

        f.write(lid)
        for line in seq_d[lid]:
            f.write(line)