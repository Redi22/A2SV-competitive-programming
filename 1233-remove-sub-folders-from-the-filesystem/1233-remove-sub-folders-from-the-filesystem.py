class TrieNode:
    def __init__(self):
        self.isEOW = False
        self.children = defaultdict(int)

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        word = word.split("/")
        
        for letter in word:
            if cur.isEOW:
                return True
                
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            
            cur  = cur.children[letter]
        cur.isEOW = True     
        return False
        

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        folder.sort()
        res = []
        
        for path in folder:
            if not root.insert(path):
                res.append(path)
        return res
        