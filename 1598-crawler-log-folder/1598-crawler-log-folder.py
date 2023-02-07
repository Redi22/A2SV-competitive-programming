class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_stack = []
        
        for operation in logs:
            if(operation == "../"):
                if folder_stack: folder_stack.pop()
                    
            elif(operation != "./"):
                folder_stack.append(operation)
                
        return len(folder_stack)
                
                