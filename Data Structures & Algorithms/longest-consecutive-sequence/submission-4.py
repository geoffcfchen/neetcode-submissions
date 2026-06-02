class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longestNumber = 1
        

        if len(nums) == 0:
            return 0

        for n in nums:
            j = n
            if (j-1) not in numSet:
                length = 1
                while (j+1) in numSet:
                    length = length +1
                    j= j+1
                longestNumber = max(longestNumber,length)
        return longestNumber
