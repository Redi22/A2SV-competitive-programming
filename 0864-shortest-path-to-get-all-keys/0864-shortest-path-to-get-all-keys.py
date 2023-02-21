class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        caps = "ABCDEF"
        lows = "abcdef"
        
        key_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '@':
                    start = [r,c]
                if grid[r][c] in lows:
                    key_count += 1
        
        def inBound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        queue = deque([(start[0], start[1], '', 0)])
        visited = set()
        directions = [(0,1), (0,-1),(-1,0),(1,0)]
        steps = 0
        while queue:
            i, j, key, step = queue.popleft()
                
            if (i, j, key) in visited:
                continue
                
            if len(key) == key_count:
                return step

            visited.add((i, j, key))

            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                if inBound(nx, ny) and grid[nx][ny] != "#": 

                    if (grid[nx][ny] in caps and grid[nx][ny].lower() in key) or grid[nx][ny] in ".@":
                        queue.append((nx, ny, key, step + 1))

                    elif grid[nx][ny] in lows:

                        if grid[nx][ny] not in key:
                            queue.append((nx, ny, key+grid[nx][ny], step + 1))
                        else:
                            queue.append((nx, ny, key, step + 1))


        return -1