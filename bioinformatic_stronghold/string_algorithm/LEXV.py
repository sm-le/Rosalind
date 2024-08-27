# Rosalind: String Algorithms
# Ordering Strings of Varying Length Lexicographically

# Question
"""
Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).

Return: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
"""

# Example
"""
DNA
3
D
DD
DDD
...
...
AA
AAD
AAN
AAA
"""
from itertools import product

def CustomSort(subject:list,
               scores:dict,
               n:int) -> list:
    """Sort subject by scores

    Args:
        subject: a subject list to be sorted
        scores: scoring dictionary
        n: expected length

    Returns:
        list(sorted subject)
    """
    # initialize subject to score mapping
    subject_dict = {i:0.0 for i in subject}
    
    # loop to go through all elements
    for s in subject:
        # go through all positions
        for i in range(n):
            try:
                subject_dict[s] += scores.get(s[i],0) / (len(scores)+1)**i
            except:
                subject_dict[s] += 0
    
    sorted_subject = sorted(subject_dict, key=subject_dict.get)

    return sorted_subject


def LetterPermutation(letter_set:list,
                      max_element:int):

    all_prod = [list(product(list(letter_set), repeat=k)) for k in range(1,max_element+1)]
    all_prod = ["".join(list(i)) for row in all_prod for i in row]
    return all_prod

def OrderLetterPermutation(letter_set:list,
                           max_element:int):
    letters = LetterPermutation(letter_set,max_element)
    scores = {l:i for i,l in enumerate(letter_set,0)}
    order_letters = CustomSort(letters, scores, max_element)
    return order_letters