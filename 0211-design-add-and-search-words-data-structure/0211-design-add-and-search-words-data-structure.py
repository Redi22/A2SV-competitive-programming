class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current  = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
            
        current["#"] = {}  
        
    def traverse(self, current, i, word):
        if i == len(word):
            return "#" in current
        if word[i] == ".":
            for key in current:
                if self.traverse(current[key], i+1, word):
                    return True
            return False
        return word[i] in current and self.traverse(current[word[i]], i+1, word)
    
    def search(self, word: str) -> bool:
        current = self.root
        return self.traverse(current, 0, word)
    
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)