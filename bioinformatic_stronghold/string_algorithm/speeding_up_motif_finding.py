"""
String Algorithm 16

Given a DNA string s (maximum 100 kbp) in fasta format, return a failure array s satistifying s[j:k] = s[1:k-j+1]

Example:
IN: CAGCATGGTATCACAGCAGAG
OUT: 0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
"""

from tools.fasta_reader import FastaFile

def motif_finder_v1(path:str) -> str:
    """motif finder

    Args:
        path: path to fasta file

    Returns:
        str(result path)
    """

    partials = dict()

    # make pattern array with subject sequence
    with FastaFile(path) as f:
        for record in f.body:
            seq = record['sequence']

            for i in range(1,int(len(seq)/2)+1):
                partial = seq[:i]
                partials[partial] = len(partial)

    # prepare empty array
    f_array = [0] * len(seq)

    # nested for loop to iterate every pattern without first character in subject sequence
    for ub in range(1, len(seq)):
        to_advance = False
        for lb in range(1, len(seq) - ub):
            f_len = 0
            if seq[lb:lb+ub] in partials:
                f_len = partials[seq[lb:lb+ub]]
                f_array[lb+ub-1] = f_len
                to_advance = True

        # if no new array, break      
        if to_advance is False:
            break

    # save output in same directory
    p = path.split("/")[0]
    with open(f"{p}/result.txt", "w") as f:
        for i in f_array:
            f.write(f"{i} ")