class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for n in nums:
            if n in check:
                return True
            else:
                check.add(n)
        return False
            