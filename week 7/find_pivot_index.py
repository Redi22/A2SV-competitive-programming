class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      
        bSum = [0]
        total = 0
        result = []
    
        for i in range(len(nums)-1,0,-1):
            total += nums[i]
            bSum.append(total)
        total = 0
        print(bSum)
        for i in range(len(nums)): 
            print(total , bSum[-1])
            if(total == bSum.pop()):
                return i
            total += nums[i]
           
        return -1