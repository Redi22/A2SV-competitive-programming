class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""
        
        l = 0
        countT = Counter(t)
        countS = defaultdict(int)
        minn = float("inf")
        ans = [-1,-1]
        have = 0
        need = len(countT)
        
        for r in range(len(s)):
            ch = s[r]
            countS[ch] += 1
            
            if ch in countT and countT[ch] == countS[ch]:
                have += 1
                
            while have == need:
                if (r - l + 1) < minn:
                    minn = (r - l + 1) 
                    ans = [l, r]
                    
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        return s[ans[0]: ans[1]+1] if minn != float("inf") else ""
                
                