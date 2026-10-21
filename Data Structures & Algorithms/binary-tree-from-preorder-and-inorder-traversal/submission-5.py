# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pre = collections.deque(preorder)
        n = len(preorder)

        indices  = {val:idx for idx,val in enumerate(inorder)}


        def dfs(start, end):
            if start > end:
                return None
            node = pre.popleft()
            root = TreeNode(node)
            middle = indices[node]
            root.left = dfs(start, middle-1)
            root.right = dfs(middle+1, end)

            return root
        
        return dfs(0,n-1)
#         preorder = [1,2,3,4]
#         inorder = [2,1,3,4]

#         1 
#     2       3,
# [] []       []  4
