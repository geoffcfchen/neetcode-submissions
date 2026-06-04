class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # let's first find the pivot index
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        # determine which side should we go for

        if nums[pivot] <= target <= nums[len(nums)-1]:
            l, r = pivot, len(nums)-1
        else:
            l, r = 0, pivot -1
        
        ## normal binary search for sorted list to find target

        # 3. Normal binary search
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1




