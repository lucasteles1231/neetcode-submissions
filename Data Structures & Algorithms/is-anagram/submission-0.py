class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for i in list(s):
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1

        dict_t = {}
        for i in list(t):
            if i in dict_t:
                dict_t[i] += 1
            else:
                dict_t[i] = 1

        if dict_t == dict_s:
            return True
        
        return False