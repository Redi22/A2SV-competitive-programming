class Solution:
    def find(self, node, parent):
        if parent[node] == node:
            return node
        parent[node] = self.find(parent[node], parent)
        
        return parent[node]
    
    def union(self, node1, node2, parent, rank):
        parent1 = self.find(node1, parent)
        parent2 = self.find(node2, parent)
        
        if rank[parent1] < rank[parent2]:
            parent[parent1] = parent2
            rank[parent2] += rank[parent1]
        else:
            parent[parent2] = parent1
            rank[parent1] += rank[parent2]
    
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [tuple(stone) for stone in stones]
        parent = defaultdict(tuple)
        rank = defaultdict(int)
        count = 0
        
        for stone in stones:
            parent[stone] = stone
            
        for stone1 in stones:
            for stone2 in stones:
                if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                    self.union(stone1, stone2, parent, rank)

        for single_parent in parent:
            if parent[single_parent] == single_parent:
                count += 1
                
        return len(stones) - count