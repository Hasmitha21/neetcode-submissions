class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = [False] * (len(s) + 1)
        # dp[len(s)] = True
        # for i in range(len(s)-1,-1,-1):
        #     for w in wordDict:
        #         if (i + len(w) <= len(s) and s[i:i+len(w)] == w):
        #             dp[i] = dp[i+len(w)]
        #         if dp[i]:
        #             break
        # return dp[0]

        #BruteFORCE
        # def dfs(i):
        #     if i == len(s):
        #         return True
        #     for w in wordDict:
        #         if((i+len(w)) <= len(s) and s[i: i+len(w)] == w):
        #             if dfs(i + len(w)):
        #                 return True
        #     return False
        
        # return dfs(0)

        queue = collections.deque([s])
        visited = set()
        while queue:
            word = queue.popleft()
            if word in visited:
                continue
            else:
                if not word:
                    return True
                visited.add(word)
                for w in wordDict:
                    if word.startswith(w):
                        queue.append(word[len(w):])
        return False


        