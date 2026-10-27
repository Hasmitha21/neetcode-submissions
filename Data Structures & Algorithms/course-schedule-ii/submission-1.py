class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = { i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        res = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in visited:
                return True
            
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for i in range(len(preMap[crs])):
                if not dfs(preMap[crs][i]):
                    return False
            
            visited.add(crs)
            cycle.remove(crs)
            res.append(crs)
            return True


        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res