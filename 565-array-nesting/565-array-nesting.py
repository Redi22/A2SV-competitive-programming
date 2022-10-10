class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        parent = [-1] * n
        
        def find(u):
            while parent[u] > 0:
                u = parent[u]
            return u
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu != -1 and pu != pv:
                if parent[pu] < parent[pv]:
                    parent[pu] += parent[pv]
                    parent[pv] = pu
                else:
                    parent[pv] += parent[pu]
                    parent[pu] = pv

        
        for i, val in enumerate(nums):
            union(i, val)
            
        return -min(parent)