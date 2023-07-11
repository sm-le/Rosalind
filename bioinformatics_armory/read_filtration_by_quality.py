"""
# read filtration by quality

Given quality threshold, percentage of bases, fastq format, return the number of reads passing the thresholds

Example,
IN: 
    20 90
    @Rosalind_0049_1
    GCAGAGACCAGTAGATGTGTTTGCGGACGGTCGGGCTCCATGTGACACAG
    +
    FD@@;C<AI?4BA:=>C<G=:AE=><A??>764A8B797@A:58:527+,
    @Rosalind_0049_2
    AATGGGGGGGGGAGACAAAATACGGCTAAGGCAGGGGTCCTTGATGTCAT
    +
    1<<65:793967<4:92568-34:.>1;2752)24')*15;1,.3*3+*!
    @Rosalind_0049_3
    ACCCCATACGGCGAGCGTCAGCATCTGATATCCTCTTTCAATCCTAGCTA
    +
    B:EI>JDB5=>DA?E6B@@CA?C;=;@@C:6D:3=@49;@87;::;;?8+
OUT:
    2
"""

from tools.fastq import Fastq

def get_passed_record(file:str, threshold:int, percentage:int) -> int:
    """Get passed fastq record

    Args:
        file: fastq file
        threshold: base quality threshold
        percentage: percentage of bases passing threshold
    Returns:
        int(count(removed))
    """

    f = Fastq(file)
    f._parse()
    m = f._baseclean(threshold,percentage)

    return m