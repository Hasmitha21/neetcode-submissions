# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # -- DFS --

        # if not root:
        #     return None
        
        # temp = root.left
        # root.left = root.right
        # root.right = temp
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        # -- BFS --

        if not root:
            return None
        
        q = collections.deque()
        q.append(root)
        while q:
            n = q.popleft()
            temp = n.left
            n.left = n.right
            n.right = temp
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return root