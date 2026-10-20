# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        nodes = []
        # res = 0

        def dfs(node):
            if not node:
                return
            
            nodes.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        nodes.sort()
        return nodes[k-1]
        # for i in range(len(nodes)-k):
        #     return nodes[i]