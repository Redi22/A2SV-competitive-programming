class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        
        '''
        res = []
        i = 0
        size = 0
        line = []
        
        while i < len(words):
            current = words[i]
            
            if size + len(current) <= maxWidth:
                line.append(current)
                size += len(current) + 1
                i += 1
            else:
                spaces = maxWidth - (size - 1) + len(line) - 1           
                j = 0
                added = 0
                while added < spaces:
                    if j >= (len(line) - 1):
                        j = 0
                    
                    line[j] += " "
                    added += 1
                    j += 1
                
                res.append("".join(line))            
                line = []
                size = 0
                
        for word in range(len(line) - 1):
            line[word] += " "
        
        line[-1] += " " * (maxWidth - size + 1)
        res.append("".join(line))
        
        return res
        
        
        
        