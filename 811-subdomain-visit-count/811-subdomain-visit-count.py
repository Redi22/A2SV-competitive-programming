class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = Counter()
        res = []
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count

        for dom, ct in ans.items():
            res.append(str(ct) + " " + dom)
        
        return res
            
            
            