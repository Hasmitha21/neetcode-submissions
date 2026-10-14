class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # -- Brute Force -- # O(n * 2^n)

        # res = set()
        # def backtrack(i, subset):
        #     if i == len(nums):
        #         res.add(tuple(subset))
        #         return
        #     subset.append(nums[i])
        #     backtrack(i+1, subset)
        #     subset.pop()
        #     backtrack(i+1, subset)
        
        # nums.sort()
        # backtrack(0,[])
        # return [list(sub) for sub in res]


        # -- Backtracking without set() -- #

        res = []

        nums.sort()

        def dfs(i,subset):
            #base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, subset)
        
        dfs(0, [])
        return res
