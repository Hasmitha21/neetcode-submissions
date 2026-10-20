# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # -- dfs

        # def valid(node, left, right):
        #     if not node:
        #         return True
            
        #     if not (node.val < right and node.val > left):
        #         return False
            
        #     return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        

        # return valid(root, float("-inf"), float("inf"))


        # -- BFS

        if not root:
            return True
        
        q = collections.deque()
        q.append((root,float("-inf"), float("inf")))
        while q:
            node, left, right = q.popleft()
            if not ( node.val > left and node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:    
                q.append((node.right, node.val, right))
            
        return True
