class TrieNode:
    def __init__(self):
        self.num = None
        self.zero = None
        self.one = None
        

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        maxx = 0
        for num in nums:
            curr = root
            for b in range(31, -1, -1):
                bit = num & (1 << b)
                if bit == 0:
                    if not curr.zero:
                        curr.zero = TrieNode()
                    curr = curr.zero
                else:
                    if not curr.one:
                        curr.one = TrieNode()
                    curr = curr.one
                    
            curr.num = num
            
        for num in nums:
            curr = root
            for b in range(31, -1, -1):
                bit = num & (1 << b)
                if bit == 0:
                    if curr.one:
                        curr = curr.one
                    else:
                        curr = curr.zero
                else:
                    if curr.zero:
                        curr = curr.zero
                    else:
                        curr = curr.one
                        
            maxx = max(curr.num ^ num, maxx)
        return maxx
                    
                    
                    