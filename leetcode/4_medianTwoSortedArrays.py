from typing import List
import math
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = sorted(nums1 + nums2)
    numsL = len(nums) / 2
    if numsL % 1 != 0:
        return nums[math.floor(numsL)]
    return nums[numsL]