class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #RECURSIVE o(N!)
        # def dfs(i):
        #     if i == len(nums)-1:
        #         return True
        #     jump_end = min(len(nums)-1, i+nums[i])
        #     for j in range(i+1, jump_end+1):
        #         if dfs(j):
        #             return True
        #     return False
        
        # return dfs(0)

        # DP TOP DOWN -- O(n^2)
        # memo ={}
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     if i == len(nums)-1:
        #         return True
        #     if nums[i] == 0:
        #         return False
        #     jump_end = min(len(nums)-1, i+ nums[i])
        #     for j in range(i+1, jump_end+1):
        #         if dfs(j):
        #             memo[i] = True
        #             return True
        #     memo[i] = False
        #     return False
        
        # return dfs(0)


        # GREEDY - o(n)
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0