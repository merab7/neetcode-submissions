class Solution:
    def topKFrequent(self, nums:List[int], k: int) -> List[int]:
        seen_qty = {}
       
        for i in nums: 
            if i in seen_qty:
                seen_qty[i]+=1
            else:
                seen_qty[i] = 1
        c = k
        max_v = 0
        max_k = 0
        res = []
        while c > 0:
            for k,v in seen_qty.items():
                if v > max_v:
                    max_v = v
                    max_k = k
            res.append(max_k)
            del(seen_qty[max_k])
            max_v = 0
            max_k = 0
            c-=1
            
        return res
