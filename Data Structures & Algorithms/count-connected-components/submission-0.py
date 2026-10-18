class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        visited = [False] * n
        components = 0
        for node,edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)
        def dfs(i):
            for nei in adj[i]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1
        return components