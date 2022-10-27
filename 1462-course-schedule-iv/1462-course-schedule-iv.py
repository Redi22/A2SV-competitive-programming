class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        canReach from course1 to course2 
        
        '''
        lookup = [[float("inf")] * numCourses for i in range(numCourses)]
        answer = []
        
        for frm, to in prerequisites:
            lookup[frm][to] = 1
            
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    lookup[i][j] = min(lookup[i][j], lookup[i][k] + lookup[k][j])
                    
        
        for frm, to in queries:
            answer.append(lookup[frm][to] != float("inf"))
            
        return answer