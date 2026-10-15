class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        # --- Backtracking ---

        # res = []

        # def dfs(i,curr_str):
        #     if len(curr_str) == len(digits):
        #         res.append(curr_str)
        #         return

        #     for c in digitsToChar[digits[i]]:
        #         dfs(i+1, curr_str + c)
        
        # if digits:
        #     dfs(0,"")
        # return res

        # --- Iterative BFS ---

        res = [""]

        if not digits:
            return []

        for digit in digits:
            temp =[]
            for curr_str in res:
                for c in digitsToChar[digit]:
                    temp.append(curr_str + c)
            res = temp
        return res