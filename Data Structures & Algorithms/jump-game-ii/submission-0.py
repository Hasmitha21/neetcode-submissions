class Solution:
    def jump(self, nums: List[int]) -> int:

        # DP
        memo = {}
        def dfs(i):
            if i == len(nums)-1:
                return 0
            if i in memo:
                return memo[i]
            if nums[i] == 0:
                return float("inf")
            
            res = float("inf")
            jump_end = min(len(nums)-1, i+nums[i])
            for j in range(i+1, jump_end+1):
                res = min(res, 1 + dfs(j))
            memo[i] = res
            return res
        
        return dfs(0)