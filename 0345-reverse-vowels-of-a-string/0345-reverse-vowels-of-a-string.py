class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        temp = list(s)
        i = 0
        j = len(temp) - 1
        
        while i < j:
            while i < j and temp[i] not in vowels:
                i += 1
            while j > i and temp[j] not in vowels:
                j -= 1
            temp[i], temp[j] = temp[j], temp[i] 
            i += 1
            j -= 1
            
        return ''.join(temp)