# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive DFS
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        
        # is_same = (self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))
        # return is_same

        #___________ ITERATIVE APPROACH ______________

        # if not p and not q:
        #     return True
        
        # if not q or not q:
        #     return False
        
        # if p.val != q.val:
        #     return False
        
        queue = collections.deque()
        # queue = deque([(p,q)])
        queue.append((p,q))
        while queue:
            p_node, q_node = queue.popleft()

            if not p_node and not q_node:
                continue
            
            if not p_node or not q_node:
                return False
            
            if p_node.val != q_node.val:
                return False
            
            queue.append((p_node.left,q_node.left))
            queue.append((p_node.right,q_node.right))
        
        return True
        




        