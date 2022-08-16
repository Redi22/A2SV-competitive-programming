class TrieNode:
    def __init__(self):
        self.isEOW = False
        self.children = defaultdict(int)

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
        cur =  self.root
        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                return False
        return cur.isEOW 

    def startsWith(self, prefix: str) -> bool:
        cur =  self.root
        for letter in prefix:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)