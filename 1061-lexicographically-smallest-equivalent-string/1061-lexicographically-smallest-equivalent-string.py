class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        self.parent = [i for i in range(26)]
        # self.rank = { i:1 for i in range(26)}

        # pass in relative position of a char, eg, use 0 for a and 1 for b
        # similarly it returns a relative number
        def find(curr):
            while self.parent[curr] != curr:
                curr = self.parent[curr]
            return curr

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if px < py: self.parent[py] = px
                else: self.parent[px] = py
               
        
        for c1, c2 in zip(s1, s2):
            # print(ord(c1), ord('a'))
            union(ord(c1)-ord('a'), ord(c2)-ord('a'))
        
        arr = []
        for char in baseStr:
            relative_num = find(ord(char)-ord('a'))
            arr.append(chr(relative_num + ord('a')))
        return ''.join(arr)
        