class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        
        for a in arr:
            #if input has duplicates
            if len(set(a)) < len(a): continue
            a = set(a)
            
            #for each of the combined strings
            for c in dp[:]:
                #if they have a character intersection continue
                if a & c: continue
                dp.append(a | c)
                
        return max(len(a) for a in dp)