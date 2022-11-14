class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for frm, to in dislikes:
            graph[frm].append(to)
            graph[to].append(frm)

        colors = defaultdict(bool)
        
        for person in range(1, n + 1):
            if person not in colors and person in graph:
                queue = deque([(person, True)])
                colors[person] = True
                
                while queue:
                    current, color = queue.popleft()
                    
                    for neighbour in graph[current]:
                        
                        if neighbour not in colors:
                            colors[neighbour] = not color
                            queue.append((neighbour, not color))
                        elif colors[neighbour] == color:
                            return False
                        

        return True