# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # -- DFS --
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # -- Iterative DFS -- using stack -- preorder(root, left, right)
        # if not root:
        #     return 0
        
        # stack =[[root,1]]
        # res = 1

        # while stack:
        #     node, depth = stack.pop()
        #     if node:
        #         res = max(res,depth)
        #         stack.append([node.left,depth+1])
        #         stack.append([node.right,depth+1])
        # return res



        # --- BFS --- USING QUEUE
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        depth = 0
        while q:
            for i in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            depth += 1
        return depth


        