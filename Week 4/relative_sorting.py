class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        self.arr2=arr2
        arr1.sort(key=self.check_index)
        return arr1
    
    def check_index(self, value):
        priority=[0,0]
        if value in self.arr2:
            priority[1]=self.arr2.index(value)+1
        else:
            priority[0]=value
        return priority