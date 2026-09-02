class Solution:
    def topKFrequent(self, nums:List[int], k: int) -> List[int]:
        count_dict = {}
        f_list = [[] for _ in range(len(nums) + 1)]
        res = []
        for i in nums:
            count_dict[i] = 1 + count_dict.get(i, 0)
        for n, c in count_dict.items():
            f_list[c].append(n)
        for f in range(len(f_list)-1, 0, -1):
            for n in f_list[f]:
                res.append(n)
                if len(res) == k :
                    return res





        # seen_qty = {}
       
        # for i in nums: 
        #     if i in seen_qty:
        #         seen_qty[i]+=1
        #     else:
        #         seen_qty[i] = 1
        # c = k
        # max_v = 0
        # max_k = 0
        # res = []
        # while c > 0:
        #     for ky,v in seen_qty.items():
        #         if v > max_v:
        #             max_v = v
        #             max_k = ky
        #     res.append(max_k)
        #     del seen_qty[max_k]
        #     max_v = 0
        #     max_k = 0
        #     c-=1
            
        # return res
