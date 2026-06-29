class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            if n not in hashMap:
                m = target - n
                hashMap[m] = i
            else:
                return [hashMap[n],i]