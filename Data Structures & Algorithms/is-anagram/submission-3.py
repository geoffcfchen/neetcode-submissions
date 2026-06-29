class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## the following solution is O(nlog(n))
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # if len(sorted_s) != len(sorted_t):
        #     return False
        # for i in range(len(sorted_s)):
        #     if sorted_s[i] != sorted_t[i]:
        #         return False
        # return True

        ## do O(n)
        if len(s) != len(t):
            return False
        
        hashMap_s = {}
        hashMap_t = {}
        for n in s:
            if n in hashMap_s:
                hashMap_s[n] += 1
            else:
                hashMap_s[n] = 0
        for n in t:
            if n in hashMap_t:
                hashMap_t[n] += 1   
            else:
                hashMap_t[n] = 0
        if hashMap_s == hashMap_t:
            return True
        else:
            return False
        

