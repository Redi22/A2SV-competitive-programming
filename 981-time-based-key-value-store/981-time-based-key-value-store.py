from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.keyDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyDict:
            self.keyDict[key] = SortedDict()
        
        self.keyDict[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keyDict:
            return ""
        
        timestamps = list()
        newKey = self.keyDict[key].bisect_right(timestamp)
        return self.keyDict[key].peekitem(newKey - 1)[1] if newKey > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)