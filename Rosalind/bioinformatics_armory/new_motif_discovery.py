"""
# Armory 3

Given a set of protein strings in FASTA format, return regular expression for the best-scoring motif.

Example,
IN: 
    >a_1
    AGSDGHSKEHKESHFKE
    >a_2
    AGSDGHSKEHKESHDKE
    >a_3
    AGSDGHSKEHKESHFKE
OUT:
    AGSDGHSKEHKESH[FD]KE
"""

import re
from tools.meme import meme

def motif_finder_with_meme(file:str, out_path:str, minw:int=15, maxw:int=50):
    """Find motif with MEME program

    Args:
        file: file
        out_path: output path
        minw: minimum width
        maxw: maximum width
    """

    std_out = meme(file, out_path, minw, maxw)

    target_text = str()

    with open(std_out, "r") as f:
        for line in f:
            if line.strip().endswith("regular expression"):
                target_text += line
                target_text += next(f)
                target_text += next(f)

    rst = re.search(r"regular expression[\n\s].+\n([A-Z\S]+)", target_text).group(1)

    return rst

from tools.fasta_reader import FastaFile
from tools.overlap_assembly import assembly
from tools.hamming_distance import hamming_distance_v1 as hd

def in_progess_motif_finder(seed_length:int, min_cov:float, max_dist:int) -> str:
    """Motif finder 
    ** in progress ** 
    code development is under progress, unfinished code.

    Args:
        seed_length: minimum k-mer length to finder (a) motif(s).
        min_cov: minimum coverage for exact matching motif
        max_dist: maximum difference between one motif to other motif.
    
    Returns:
        str(regex(motif))
    """
    with FastaFile('example_dataset/rosalind_meme.txt') as fa:
        records = fa.body
        

    kmer_aa = dict()

    for record in records:
        for idx in range(len(record['sequence'])-seed_length):
            kmer = record['sequence'][idx:idx+seed_length]

            try:
                kmer_aa[kmer] += 1
            except:
                kmer_aa[kmer] = 1


    fkmer_aa = list(dict(filter(lambda x: x[1] > len(records) * min_cov, kmer_aa.items())).keys())
    asm_aa = assembly(fkmer_aa)

    motifs = set()

    for record in records:
        for idx in range(len(record['sequence'])-len(asm_aa)):
            comp_aa = record['sequence'][idx:idx+len(asm_aa)]

            hmd = hd(comp_aa, asm_aa)

            if hmd < max_dist:
                motifs.add(comp_aa)

    rgx = str()

    if len(motifs) == 2:
        motifs = list(motifs)
        for s1, s2 in zip(motifs[0], motifs[1]):
            if s1 == s2:
                rgx += s1
            elif s1 != s2:
                rgx += f"[{s1}{s2}]"

    else:
        print("haven't developed a code for this case. Will come back later")
