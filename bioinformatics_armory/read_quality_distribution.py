"""
# read quality distribution

Given quality threshold and fastq format, return the number of reads below quality threshold

Example,
IN: 
    28
    @Rosalind_0041
    GGCCGGTCTATTTACGTTCTCACCCGACGTGACGTACGGTCC
    +
    6.3536354;.151<211/0?::6/-2051)-*"40/.,+%)
OUT:
    1
"""

from tools.fastq import Fastq

def get_removed_record(file:str, threshold:int) -> int:
    """Get removed fastq record

    Args:
        file: fastq file
        threshold: base quality threshold
    Returns:
        int(count(removed))
    """

    f = Fastq(file)
    f._parse()
    m = f._avgclean(threshold)

    return m