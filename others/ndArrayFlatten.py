from typing import List
def flattenArr(arr:List[int|str]) -> List[int|str]:
    """Flatten any n-dimensional array

    Args:
        arr: n-dimensional array
    Returns:
        list(flatten arr)
    """
    rc_arr = list()
    i = 0
    while i < len(arr):
        if not isinstance(arr[i], list):
            rc_arr.append(arr[i])
            i += 1
        else:
            rc_arr += flattenArr(arr[i])
            i += 1
        
    return rc_arr