class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        red_dict = {}
        res = {}
        res_list = []
       
        for s in strs:
            s_ed = ''.join(sorted(s))
            if s_ed in red_dict:
                val = red_dict[s_ed]
                val.append(s)
                red_dict[s_ed] = val
            else:
                red_dict[s_ed] = []
        seen = set()
        for s in strs:
            s_ed = ''.join(sorted(s))
            if s_ed in red_dict and s_ed not in seen:
                res[s] = red_dict[s_ed]
                seen.add(s_ed)
        # res_list = [[k] if not v else [[k] + v] for k, v in res.items()]
        for k, v in res.items():
            if not v:
                res_list.append([k])
            else:
                res_list.append([k] + v)
    
        return res_list
