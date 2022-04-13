class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegrees = [0] * numCourses
        outgoing = defaultdict(set)
        queue = deque()
        res = []
        
        for course, pre in prerequisites:
            outgoing[pre].add(course)
            
            inDegrees[course] += 1

        for i in range(numCourses):
            if inDegrees[i]==0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            res.append(course)
            for neighbor in outgoing[course]:
                inDegrees[neighbor]-=1
                if inDegrees[neighbor]==0:
                    queue.append(neighbor)
        if len(res) != numCourses:
            return []
        return res
