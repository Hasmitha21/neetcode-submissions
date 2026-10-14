class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # Brute Force O(n*2^n)

        # res = set()
        # candidates.sort()

        # def generate_subsets(i, curr, totalsum):
        #     if totalsum == target:
        #         res.add(tuple(curr))
        #         return
        #     if totalsum > target or i == len(candidates):
        #         return
            
        #     curr.append(candidates[i])
        #     generate_subsets(i+1, curr, totalsum + candidates[i])

        #     curr.pop()
        #     generate_subsets(i+1, curr, totalsum)
        
        # generate_subsets(0, [], 0)
        # return [list(combination) for combination in res] 


        # Backtracking

        res = []
        candidates.sort()
        def dfs(i, curr, totalsum):
            if totalsum == target:
                res.append(curr.copy())
                return
            if totalsum > target or i >= len(candidates):
                return
            
            #include candidates[i]
            curr.append(candidates[i])
            dfs(i+1, curr, totalsum + candidates[i])

            #skip candidates[i]
            curr.pop()
            while i+1 <len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr, totalsum)
        
        dfs(0, [], 0)
        return res