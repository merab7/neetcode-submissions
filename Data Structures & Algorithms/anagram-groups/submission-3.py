class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_key_dict = {}
        res_dict = {}
        res_list = []
       
        for s in strs:
            s_ed = ''.join(sorted(s))
            if s_ed in sorted_key_dict:
                val = sorted_key_dict[s_ed]
                val.append(s)
                sorted_key_dict[s_ed] = val
            else:
                sorted_key_dict[s_ed] = []
        
        seen = set()
        #სეტი იმიტომ რომ შეიძლება შესადარებელი ვალიუ იყოს რამდენიმე აითემის 
        #დაშორებით და შესაბამისად ნანახებო უნდა დავიმახსოვროთ და 
        #შევადაროთ როცა უბრალოდ სტრინგი იყო ყოველთვის იცვლებოდა 
        #შესაბამისად გამოტოვებით თუ იყო ითემი ძველი არსებული იკარგებოდა
        
        for s in strs:
            s_ed = ''.join(sorted(s))
            if s_ed in sorted_key_dict and s_ed not in seen:
                res_dict[s] = sorted_key_dict[s_ed]
                seen.add(s_ed)
        
        for k, v in res_dict.items():
            if not v:
                res_list.append([k])
            else:
                res_list.append([k] + v)
    
        return res_list
