class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l, subL, res = len(words[0]) * len(words), len(words[0]), []
        subs, count = Counter(words), defaultdict(int)
        
        for i in range(len(s)):
            temp = s[i:i + l]
            count = defaultdict(int)
            
            for j in range(0, len(temp), subL):
                temp2 = temp[j:j + subL]
                count[temp2] += 1
                
            if count == subs:
                res.append(i)
                
        return res