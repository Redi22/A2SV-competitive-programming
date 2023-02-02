class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        position = {character : i for i, character in enumerate(order)}
        l = [[position[wi] for wi in word] for word in words]
        
        for i in range(len(l)):
            for j in range(1, len(l)):
                if l[i] > l[j]:
                    return False
                
        return True