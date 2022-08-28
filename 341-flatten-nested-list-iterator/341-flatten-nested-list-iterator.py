# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque([])
        for item in nestedList:
            self.populate(item)
        
    def populate(self, nestedList: [NestedInteger]):
        if nestedList.isInteger():
            self.queue.append(nestedList.getInteger())
        else:
            for item in nestedList.getList():
                self.populate(item)
    
    def next(self) -> int:
        return self.queue.popleft()
    
    def hasNext(self) -> bool:
         return len(self.queue) != 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())