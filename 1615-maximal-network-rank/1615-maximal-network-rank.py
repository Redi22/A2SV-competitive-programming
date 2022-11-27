class Solution:
    def getNetworkRank(self, city1,  city2, graph):
        rank = len(graph[city1])
        for node in graph[city2]:
            rank += node != city1
            
        return rank
        
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maximal_rank = float("-inf")
        graph = defaultdict(set)
        
        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
            
        for city1 in range(n):
            for city2 in range(n):
                if city1 != city2:
                    rank = self.getNetworkRank(city1, city2, graph)
                    maximal_rank = max(maximal_rank, rank)
                
        return maximal_rank