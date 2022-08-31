class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        
        for st in strs:
            key = "".join(sorted(st))            
            dictionary[key].append(st)
            
        return [dictionary[s] for s in dictionary]