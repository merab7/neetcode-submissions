class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        look_up_dict = {}

        for num in nums:
            if num in look_up_dict:
                return True
            else:
                look_up_dict[num]=num
        return False 
            

        