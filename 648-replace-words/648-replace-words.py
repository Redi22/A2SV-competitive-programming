class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEOW = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
                
            cur  = cur.children[letter]
        cur.isEOW = True       
        

    def search(self, word: str) -> bool:
        w = []
        cur =  self.root
        for letter in word:
            if cur.isEOW:
                return "".join(w)
            if letter in cur.children:
                w.append(letter)
                cur = cur.children[letter]
            else:
                return False 
        

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        ans = []
        for word in dictionary:
            root.insert(word)
            
        sentence = sentence.split(' ')
        for word in sentence:
            temp = root.search(word)
            if temp:
                ans.append(temp)
            else:
                ans.append(word)
            ans.append(" ")
        
        return "".join(ans[:-1])
        