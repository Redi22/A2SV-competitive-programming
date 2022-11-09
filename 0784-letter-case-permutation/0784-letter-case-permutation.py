class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        '''
        count the letters
        vary from 1 to 2 ** count - 1
        apply the bits to the letters only 
        set bit means swap 
        
        
        '''
        count = len([si for si in s if si.isalpha()])
        limit = (2 ** count) - 1
        variants = []
        
        for i in range(limit + 1):
            result = list(s)
            shift = 0
            variant = i 
            
            for j in range(len(s) - 1, -1, -1):
                if result[j].isalpha():
                    result[j] = result[j].upper() if variant & (1 << shift) else result[j].lower()
                    shift += 1

                
            variants.append("".join(result))
            
        return variants
                
            
                
                
        
        
        
        
        