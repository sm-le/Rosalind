"""
# Base quality distribution

Given fastq file and a threshold, return number of position where base quality falls below the threshold

Example,
IN: 
    Sample Dataset
    26
    @Rosalind_0029
    GCCCCAGGGAACCCTCCGACCGAGGATCGT
    +
    >?F?@6<C<HF?<85486B;85:8488/2/
    @Rosalind_0029
    TGTGATGGCTCTCTGAATGGTTCAGGCAGT
    +
    @J@H@>B9:B;<D==:<;:,<::?463-,,
    @Rosalind_0029
    CACTCTTACTCCCTAGCCGAACTCCTTTTT
    +
    =88;99637@5,4664-65)/?4-2+)$)$
    @Rosalind_0029
    GATTATGATATCAGTTGGCTCCGAGAGCGT
    +
    <@BGE@8C9=B9:B<>>>7?B>7:02+33.
    Sample Output

OUT:
    17
"""

from tools.fastq import Fastq

def get_average_bases_under_threshold(file:str, threshold:int) -> int:
    """Get base quality under threshold

    Args:
        file: fastq file
        threshold: base quality threshold
    Returns:
        int(count(but))
    """

    f = Fastq(file)
    f._parse()
    f._getallquals()

    p = [sum([item[i] for item in f.arrays])/len(f.arrays) < threshold for i in range(len(f.arrays[0]))]
    
    return p.count(True)