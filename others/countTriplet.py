from typing import List
def triplet_counter(arr:List[int],k=int) -> int:
    """Count a number of triplets making k in a given list

    Args:
        arr: an array of intergers
        k: target k (a+b+c)
    Returns:
        int(count of triplets)
    """

    pos = list()
    cnt = 0

    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            try:
                jn = arr[j+1:].index(k-(arr[i]+arr[j]))
                pos.append((i,j,jn+1+j))
                cnt += 1
            except ValueError:
                continue
    return cnt