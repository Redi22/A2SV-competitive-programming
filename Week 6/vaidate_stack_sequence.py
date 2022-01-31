class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in range(len(pushed)):
            print(pushed[i] , popped[0])
            if pushed[i] == popped[0]:
                popped.pop(0)
                while stack and stack[-1] == popped[0]:
                    popped.pop(0)
                    stack.pop()
            elif stack and  stack[-1] == popped[0]:
                while stack and stack[-1] == popped[0]:
                    popped.pop(0)
                    stack.pop()
            else:
                stack.append(pushed[i])
            print(stack)
        print(popped)
        while stack and stack[-1] == popped[0]:
            popped.pop(0)
            stack.pop()
        return len(popped) == 0
                