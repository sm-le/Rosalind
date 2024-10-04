from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # filter to get indexes of numbers under target
        fnums = [i for i, num in enumerate(nums) if num <= abs(target)]

        # iterate through the filtered list
        found = set()

        for idx in fnums:
            if target - nums[idx] in nums:
                if idx == nums.index(target - nums[idx]):
                    continue
                found.add(idx)
                found.add(nums.index(target - nums[idx]))
                return list(found)