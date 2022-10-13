class Solution:
    def isBipartite(self, gra: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for frm, nodes in enumerate(gra):
            for to in nodes:
                graph[frm].append(to)
                graph[to].append(frm)

        colors = defaultdict(bool)
        ans = 1
        n = len(gra)
        
        for i in range(1, n + 1):
            if i not in colors and i in graph:
                queue = deque([(i, True)])
                colors[i] = True
                while queue:
                    curr, color =  queue.popleft()


                    for nei in graph[curr]:

                        if nei not in colors:
                            colors[nei] = not color
                            queue.append((nei, not color))
                        else:
                            if colors[nei] == color:
                                return False

        return True