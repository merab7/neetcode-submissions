class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_dict = {x:s.count(x) for x in s}
        t_dict = {x:t.count(x) for x in t}
         
        for char, count in t_dict.items():
            if char not in s_dict or char in s_dict and count != s_dict[char]:
                return False
        return True
        