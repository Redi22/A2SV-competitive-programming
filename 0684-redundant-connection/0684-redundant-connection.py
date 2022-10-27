class Solution:
    def find(self, node, parent):
            current = node
            if parent[current] < 0:
                return current
            
            parent[current] = self.find(parent[current], parent)
            
            return parent[current]
        
    def union(self, node1, node2, parent):
        pu = self.find(node1, parent)
        pv = self.find(node2, parent)

        if pu != -1 and pu != pv:
            if parent[pu] < parent[pv]:
                parent[pu] += parent[pv]
                parent[pv] = pu
            else:
                parent[pv] += parent[pu]
                parent[pu] = pv
            return True
        
        return False 
        
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1] * (len(edges) + 1)
        answer = [-1, -1]
        
        for frm, to in edges:
            if not self.union(frm, to, parent):
                answer = [frm, to]
                
        # print(parent)
        return answer
                
        