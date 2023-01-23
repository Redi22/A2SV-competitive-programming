class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(int)
        trusted = defaultdict(int)
        
        for a,b in trust:
            trusts[a] += 1
            trusted[b] += 1
            
        for i in range(1, n+1):
            if i not in trusts and trusted[i] == n - 1:
                return i
            
        return -1