class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        original_roads = set()
        bidirectional_roads = defaultdict(list)
        
        for src, dst in connections:
            original_roads.add((src, dst))
            bidirectional_roads[src].append((dst, 1))
            bidirectional_roads[dst].append((src, 0))
            
        queue = deque([0])
        count = 0
        visited = set([0])
        
        while queue:
            node = queue.popleft()
            for neighbour, cost in bidirectional_roads[node]:
                if neighbour not in visited:
                    count += cost
                    queue.append(neighbour)
                    visited.add(neighbour)

        return count