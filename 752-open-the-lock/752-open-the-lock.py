class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = []
        visited = set()
        step = 0
        nodes = ["0", "1","2","3","4","5","6","7","8","9"]
        deadends = set(deadends)
        
        if "0000" not in deadends: queue.append("0000")
            
        while queue:
            newLevel = []
            for node in queue:
                if node == target:
                    return step
                
                for i in range(4):
                    nodeVal = int(node[i])
                    
                    if nodeVal == 9:
                        nodeVal = 0
                        
                    neww = node[:i] + nodes[nodeVal + 1] + node[i + 1:]
                    if neww not in visited and neww not in deadends:
                        newLevel.append(neww)
                        visited.add(neww)
                    
                    neww = node[:i] + nodes[int(node[i]) - 1] + node[i + 1:]
                    if neww not in visited and neww not in deadends:
                        newLevel.append(neww)
                        visited.add(neww)
                
            queue = newLevel
            step += 1
            
        return -1