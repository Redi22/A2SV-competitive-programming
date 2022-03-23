
        
    
class Solution:
        """
        ababcbacadefegdehijhklij
        0123456789
        a = 0 8
        b = 1 5 
        c = 4 7 
        
        0 8
        d = 9 14
        e = 10 15
        f = 11 11
        g = 13 13
        9 15
        h = 16 19
        i = 17 22
        j = 17 23
        k = 19 19
        l = 20 20
        16 20
        
        """
        def partitionLabels(self, s: str) -> List[int]:
            letters = dict()
            intervals = []
            res = []

            for i in range(len(s)):
                if s[i] not in letters.keys():
                    letters[s[i]] = [i, i]
                else:
                    letters[s[i]][1] = i

            intervals = [val for val in letters.values()]

            intervals.sort()
            start, end = intervals[0][0], intervals[0][1]

            for i in range(1, len(intervals)):
                if intervals[i][0] <= end:
                    end = max(intervals[i][1], end)
                else:
                    res.append(end - start + 1)
                    start, end = intervals[i][0], intervals[i][1]
            res.append(end - start + 1)

            return res
    
    
    