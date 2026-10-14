class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Brute Force - Sorting

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        freq_arr = []
        res = []

        for n, freq in count.items():
            freq_arr.append([freq,n])
        
        freq_arr.sort()

        while len(res) <k:
            res.append(freq_arr.pop()[1])
        
        return res