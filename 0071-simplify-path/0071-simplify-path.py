class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        if / occurs last dont add
        if two or less dots occur  dont add
        
        
        '''
        valid_path = []
        
        for folder in path.split("/"):
            if valid_path and folder == "..":
                valid_path.pop()
            elif folder and folder not in [".", ".."]:
                valid_path.append(folder)
                
        valid_path = "/".join(valid_path)
        
        
        return "/" + valid_path