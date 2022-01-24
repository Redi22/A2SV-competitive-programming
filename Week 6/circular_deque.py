class MyCircularDeque:

    def __init__(self, k: int):
        self.circularDeque = [] * k
        self.queueSize = 0
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.circularDeque.insert(0, value)
            self.queueSize += 1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.circularDeque.append(value)
            self.queueSize += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.circularDeque.pop(0)
            self.queueSize -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.circularDeque.pop()
            self.queueSize -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.circularDeque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.circularDeque[-1]

    def isEmpty(self) -> bool:
        if self.queueSize == 0:
            return True
        return False
    
    def isFull(self) -> bool:
        if(self.queueSize < self.maxSize) : 
            return False
        return True
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()    