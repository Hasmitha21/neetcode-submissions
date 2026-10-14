class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # -- Brute Force -- # O(n * 2^n)

        res = set()
        def backtrack(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()
            backtrack(i+1, subset)
        
        nums.sort()
        backtrack(0,[])
        return [list(sub) for sub in res]


        # -- Backtracking without set() -- #