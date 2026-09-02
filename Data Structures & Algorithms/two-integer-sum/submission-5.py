class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v_i_map = {} #value and index map
        for i,v in enumerate(nums):
            v_to_add = target - v
            if v_to_add in v_i_map:
                return [v_i_map[v_to_add], i]
            v_i_map[v]=i
        return 

        