class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = { i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)
        

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            
            if prereqMap[crs] == []:
                return True
            
            visited.add(crs)
            for i in range(len(prereqMap[crs])):
                if not dfs(prereqMap[crs][i]):
                    return False
            visited.remove(crs)
            prereqMap[crs] = []
            return True       
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True