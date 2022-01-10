class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_mapping = {}
        isomorphic = True
        for i in range(len(s)):
            if  s[i] not in char_mapping.keys() and t[i] not in char_mapping.values():
                char_mapping[s[i]] = t[i]                
                                    
            elif s[i] in char_mapping.keys() and t[i] in char_mapping.values():
                if char_mapping[s[i]] == t[i]:
                    continue
                else:
                    isomorphic = False
                    break
            else:
                isomorphic = False
                break
                                  
        return isomorphic