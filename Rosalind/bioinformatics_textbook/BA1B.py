from typing import List
from collections import defaultdict
def frequentKmer(text:str, k=int) -> List[str]:
    """Find the most frequent kmer in the string (text)

    Args:
        text: a target text
        k: size of kmer
    Returns:
        a list of most frequent kmer (at least 1)
    """

    kmers = defaultdict(int)
    for i in range(len(text)-k+1):
        kmers[text[i:i+k]] += 1

    return [k for k, v in kmers.items() if v == max(kmers.values())]