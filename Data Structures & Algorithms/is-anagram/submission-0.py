class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmaps, hashmapt = {}, {}
        for i in range(len(s)):
            hashmaps[s[i]] = 1+hashmaps.get(s[i],0)
            hashmapt[t[i]] = 1+hashmapt.get(t[i],0)
        for i in hashmaps:
            if hashmaps[i] != hashmapt.get(i,0):
                return False
        return True

