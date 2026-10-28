class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # BRUTE FORCE - O(m*n)

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True
        
        # return False


        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot:
            cur_row = (top + bot) // 2
            if target > matrix[cur_row][-1]:
                top = cur_row + 1
            elif target < matrix[cur_row][0]:
                bot = cur_row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        cur_row = (top + bot) // 2
        l = 0
        r = COLS - 1
        while l <= r:
            mid = (l+r) // 2
            if target > matrix[cur_row][mid]:
                l = mid + 1
            elif target < matrix[cur_row][mid]:
                r = mid - 1
            else:
                return True
        
        return False