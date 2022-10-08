class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()

        def backtrack(a, b, c, d):

            if not a or not b or not c or not d:
                return 

            if len(a) > 1 and a[0] == "0":
                return
            if len(b) > 1 and b[0] == "0":
                return
            if len(c) > 1 and c[0] == "0":
                return
            if len(d) > 1 and d[0] == "0":
                return

            if 0 <= int(a) <= 255 and  0 <= int(b) <= 255 and  0 <= int(c) <= 255 and  0 <= int(d) <= 255:
                res.add(".".join([a,b,c,d]))
                return 

            
        for i in range(1,len(s)):
            for j in range(i, len(s)):
                for k in range(j, len(s)):
                    for z in range(k, len(s)):
                        backtrack(s[:i], s[i: j+1], s[j+1: k+1], s[k+1:])
                        
        return sorted(list(res))