# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # --- bfs

        res = []
        if not root:
            # res.append("N")
            return "N"
        
        q = collections.deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append("N")

        
        return ",".join(res)



        # -- DFS
        # res = []

        # def dfs(node):
        #     if not node:
        #         res.append("N")
        #         return
            
        #     res.append(str(node.val))
        #     dfs(node.left)
        #     dfs(node.right)
        
        # dfs(root)
        # return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:


        # ---- bfs
        vals = data.split(",")
        if vals[0] == "N":
            return None
        
        queue = collections.deque()
        root = TreeNode(int(vals[0]))
        queue.append(root)
        i = 1 #bc i=0 already root
        while queue:
            node = queue.popleft()
            if i < len(vals) and vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root           

        # -- DFS
        # vals = data.split(",")
        # self.i = 0

        # def dfs():
        #     if vals[self.i] == "N":
        #         self.i += 1
        #         return None
            
        #     node = TreeNode(int(vals[self.i]))
        #     self.i += 1
        #     node.left = dfs()
        #     node.right = dfs()
        #     return node
        
        # return dfs()