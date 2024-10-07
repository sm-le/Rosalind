from BA1G import hamming
from itertools import product
from typing import List
from collections import defaultdict
# brute force, maybe there is a better solution?
def frequentKmerWithMM(text:str,
                       k=int,
                       m=int) -> List[str]:
    """Find the most frequent kmer in the string (text) with mismatches

    Args:
        text: a target text
        k: size of kmer
        m: allowed mismatches
    Returns:
        a list of most frequent kmer (at least 1)
    """

    kmers = defaultdict(int)
    for i in range(len(text)-k+1):
        kmers[text[i:i+k]] += 1
    patterns = list(kmers.keys())
    nuc = ["A","T","C","G"]
    combs = (''.join(i) for i in product(nuc,repeat=k))
    kScore = defaultdict(int)
    for comb in combs:
        iScore = 0
        for pattern in patterns:
            ms = hamming(comb,pattern)
            if ms <= m:
                iScore += kmers.get(pattern)
        if iScore > 0:
            kScore[comb] = iScore
            iScore = 0
    
    maxScore = max(kScore.values())
    kScore = [k for k,v in kScore.items() if v == maxScore]
    yield from kScore