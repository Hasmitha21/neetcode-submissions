class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        curr_brackets = []

        def backtrack(open_bracket, close_bracket):
            if open_bracket == close_bracket == n:
                res.append("".join(curr_brackets))
                return
            
            if open_bracket < n:
                curr_brackets.append("(")
                backtrack(open_bracket + 1, close_bracket)
                curr_brackets.pop()
            
            if close_bracket < open_bracket:
                curr_brackets.append(")")
                backtrack(open_bracket, close_bracket + 1)
                curr_brackets.pop()
            
        backtrack(0,0)
        return res