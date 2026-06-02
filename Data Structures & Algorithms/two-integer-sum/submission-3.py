class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            findvalue = target - n
            if findvalue in hashmap:
                return ([hashmap[findvalue], i])
            hashmap[n] = i
            