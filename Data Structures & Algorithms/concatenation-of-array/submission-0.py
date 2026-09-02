class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = nums
        for i in range(len(nums)):
            new_nums.insert(len(new_nums), nums[i])
        return new_nums
        