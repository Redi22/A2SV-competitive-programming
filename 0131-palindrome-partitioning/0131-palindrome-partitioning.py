class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        @cache
        def isPalindrome(l, r):
            if l >= r:
                return True
            
            if s[l] == s[r]:
                return isPalindrome(l + 1, r - 1)
            
            return False

        
        def partition(i, path):
            if i >= len(s):
                result.append(path[:])

            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    path.append(s[i : j + 1])
                    partition(j + 1, path)
                    path.pop()

        partition(0, [])
            
        return result


