class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # ## Brute force O(n**2)
        # l, r = 0, 1
        # res = 0
        # for l in range(len(heights)):
        #     for r in range(l+1, len(heights)):
        #         area = (r-l) * min(heights[l], heights[r])
        #         res = max(area, res)
        # return res
        l, r  = 0, len(heights)-1
        res = 0 
        while l < r:
            area = (r-l) * min(heights[r], heights[l])
            res = max(res, area)
            if heights[l] > heights[r]:
                r -= 1
            elif  heights[l] < heights[r]:
                l += 1
            else:
                l += 1
        return res
            
