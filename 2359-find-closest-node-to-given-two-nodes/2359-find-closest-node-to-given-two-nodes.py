class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n1 = {node1 : 0}
        n2 = {node2 : 0}

        def dfs(i, dis, n):
            if edges[i] == -1 or edges[i] in n:
                return
            n[edges[i]] = dis + 1
            dfs(edges[i], dis + 1, n)

        dfs(node1, 0, n1)
        dfs(node2, 0, n2)

        dis = float('inf')
        res = -1

        for i in range(len(edges)):
            if i in n1 and i in n2:
                d = max(n1[i], n2[i])
                if d < dis:
                    res = i
                    dis = d
        
        return res