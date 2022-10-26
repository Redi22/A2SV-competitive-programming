class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        '''
        
        '''
        if len(connections) + 1 < n:
            return -1
        parent = [-1] * n
        
        def find(node):
            
            while parent[node] > 0:
                node = parent[node]
                
            return node
        
        def union(node1, node2):
            par1 = find(node1)
            par2 = find(node2)
            
            if par1 == par2:
                return False
            
            if par1 < par2:
                parent[par1] = par2
            else:
                parent[par2] = par1
                
            return True
        
        components = n
        for frm, to in connections:
            if union(frm, to):
                components -= 1
                
        return components - 1
            