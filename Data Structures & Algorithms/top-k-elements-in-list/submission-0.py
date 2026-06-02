class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            counts[i]= 1 + counts.get(i, 0)
        for key, value in counts.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for value in freq[i]:
                res.append(value)
                if len(res) == k:
                    return res
        


        