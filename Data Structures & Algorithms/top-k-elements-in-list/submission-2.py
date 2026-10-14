class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # ---- Brute Force - Sorting - O(n log n)

        # count = {}

        # for num in nums:
        #     count[num] = 1 + count.get(num,0)
        
        # freq_arr = []
        # res = []

        # for n, freq in count.items():
        #     freq_arr.append([freq,n])
        
        # freq_arr.sort()

        # while len(res) <k:
        #     res.append(freq_arr.pop()[1])
        
        # return res

        # --- Bucket sort O(n)

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        freq = [[] for i in range(len(nums)+1)]

        for n, cnt in count.items():
            freq[cnt].append(n)
        
        res = []

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        