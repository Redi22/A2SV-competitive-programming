class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for st in strs:
            anagrams[tuple(sorted(st))].append(st)
            
        return anagrams.values()