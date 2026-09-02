class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_m = {}
        for i, num in enumerate(nums):
            if (target - num) in seen_m:
                return [seen_m[target - num], i]
            seen_m[num] = i



        