class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        '''
        A course has 3 possible states
        1. Visited -> crs has been added to output
        2. Visiting -> crs not added to output but added to cycle
        3. Unvisited -> crs not added to output or cycle
        '''
        res = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            visited.add(crs)
            cycle.remove(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        # prereqMap = {i:[] for i in range(numCourses)}

    
        # for crs, pre in prerequisites:
        #     prereqMap[crs].append(pre)
        
        # res = []
        # visited = set()

        # def dfs(crs):
        #     if crs in visited:
        #         return False
            
        #     visited.add(crs)
        #     for pre in prereqMap[crs]:
        #         if not dfs(pre):
        #             return False
            
        #     visited.remove(crs)
        #     res.append(crs)
        
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return []
        
        # return res
        
