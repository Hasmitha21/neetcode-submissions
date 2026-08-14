# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        p = deque(preorder)
        n = len(preorder)

        lookup = {v:i for i,v in enumerate(inorder)}

        def dfs(start, end):
            if start > end:
                return None
            else:
                node = p.popleft()
                root = TreeNode(node)
                middle = lookup[node]
                root.left = dfs(start,middle-1)
                root.right = dfs(middle +1, end)
                return root
        
        return dfs(0,n-1)

  