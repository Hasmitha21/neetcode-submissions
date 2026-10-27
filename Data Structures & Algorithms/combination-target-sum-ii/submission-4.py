class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = set()
        res = []
        candidates.sort()
       
        def dfs(i, currList, totalSum):
            if totalSum == target:
                res.append(currList.copy())
                return

            if i == len(candidates) or totalSum > target:
                return 

            currList.append(candidates[i])
            dfs(i+1, currList, totalSum + candidates[i])
            currList.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, currList, totalSum)




        dfs(0, [], 0)
        return res
        