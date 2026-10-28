class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(temperatures)):
        #     warmer_found = False

        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans.append(j-i)
        #             warmer_found = True
        #             break
        #     if not warmer_found:
        #         ans.append(0)        
        # return ans
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res