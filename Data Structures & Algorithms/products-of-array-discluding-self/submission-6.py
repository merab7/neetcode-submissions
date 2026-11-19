from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = nums.count(0)
        if count_zero == 1:
            index_of_zero = nums.index(0)
            nums[index_of_zero] = 1
            product_w_zero = prod(nums)
            output = [i * 0 for i in range(len(nums)) ]
            output[index_of_zero] = product_w_zero
            return output 
        else:         
            output = []
            all_product = prod(nums)
            for i in nums:
                if i != 0:
                    output.append(int(all_product/i))
                else:
                    output.append(int(all_product))

            return output