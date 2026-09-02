class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # res = {}
        # for i in nums :
        #     if i not in res:
        #         res[i]="1"
        #     else:
        #         return  True
        # return False

        seen_num = set()
        for i in nums:
            if i in seen_num:
                return True
            seen_num.add(i)
        return False

        # return False if len(nums) == len(set(nums)) else True