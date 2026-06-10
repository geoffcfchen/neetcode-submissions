class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        countT = {}
        ## edge case
        if t == "" : return ""
        
        ## create the hashmap for string t, that is fixed information
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        l = 0
        res = [-1, -1]
        resLength = float("infinity")
        
        have, need = 0, len(countT)

        for r in range(len(s)):
            ## we need to do three things
            ## first update the window
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            ## check the condition is met or not
            if c in countT and window[c] == countT[c]:
                have += 1

            ## now if condition is met, then we keep shrinking the length and update the results
            while have == need:
                ## only update when it is smaller
                if (r-l+1) < resLength:

                    res = [l, r]
                    resLength = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in t and window[s[l]] < countT[s[l]]:
                    have = have -1
                l = l + 1
        l, r = res
        return s[l:r+1] if resLength < float("infinity") else ""


        
