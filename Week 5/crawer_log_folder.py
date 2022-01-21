class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folderStack = []
        for operation in logs:
            if(operation == "../"):
                if folderStack:
                    folderStack.pop()
            elif(operation != "./"):
                folderStack.append(operation)
        return len(folderStack)
                
                