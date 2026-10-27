class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereqMap = {i:[] for i in range(numCourses)}

        visiting = set()
        for course, pre in prerequisites:
            prereqMap[course].append(pre)
        
        def dfs(crs):

            if crs in visiting:
                return False
            
            if prereqMap[crs] == []:
                return True
            
            visiting.add(crs)
            for i in range(len(prereqMap[crs])):
                if not dfs(prereqMap[crs][i]):
                    return False
            visiting.remove(crs)
            prereqMap[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True