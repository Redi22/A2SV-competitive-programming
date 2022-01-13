class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp_stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.stack)-1 ):
            self.temp_stack.append(self.stack.pop())
        first_element = self.stack.pop()
        for i in range(len(self.temp_stack)):
            self.stack.append(self.temp_stack.pop())
        return first_element
    
    def peek(self) -> int:
        for i in range(len(self.stack)-1 ):
            self.temp_stack.append(self.stack.pop())
        first_element = self.stack.pop()
        self.stack.append(first_element)
        for i in range(len(self.temp_stack)):
            self.stack.append(self.temp_stack.pop())
        return first_element
    def empty(self) -> bool:
        if(len(self.stack) == 0):
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()