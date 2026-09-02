class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        look_up_set = set()

        for num in nums:
            if num in look_up_set:
                return True
            else:
                look_up_set.add(num)
        return False 
            

        