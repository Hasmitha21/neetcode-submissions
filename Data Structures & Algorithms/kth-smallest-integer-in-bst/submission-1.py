# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # # ---------Iteratively - Using Stack
        # n = 0 # number of elemets we visited
        # stack = []
        # cur =  root
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
            
        #     cur = stack.pop()
        #     n += 1
        #     if n == k:
        #         return cur.val
        #     cur = cur.right



# Brute Force
# collect all nodes in an array, sort them and return the kth smallest at index kk-1
        arr = []

        def dfs(root):
            if not root:
                return
            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        arr.sort()
        return arr[k-1]

