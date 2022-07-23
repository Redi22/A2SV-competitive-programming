class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        temp = float('-inf')
        ans = []
        
        for i in range(len(s)):
            if s[i] == c: 
                temp = i
            ans.append(i - temp)

        temp = float('inf')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                temp = i
            ans[i] = min(ans[i], temp - i)

        return ans