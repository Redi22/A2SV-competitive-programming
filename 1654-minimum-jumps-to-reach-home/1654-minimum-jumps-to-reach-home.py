class Solution:
    def traverse(self, forbidden, home, a, b, max_value):
        queue = [(0, 0)]
        step = 0
        visited = set()
        
        while queue:
            new_level = []
            
            for position, last in queue:
                if position < 0 or position in forbidden or position > max_value or (position, last) in visited:
                    continue

                if position == home:
                    return step

                visited.add((position, last))

                new_level.append((position + a, False))

                if not last:
                    new_level.append((position - b, True))
            queue = new_level
            step += 1
            
        return -1

    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        max_value = 2000 + a + b
        return self.traverse(forbidden, x, a, b, max_value)
        