class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        isFalse = True
        
        for i in range(len(l)):
            neww = nums[l[i]:r[i]+1]
            neww.sort()
            temp = 100001
            isFalse = True
            
            for j in range(len(neww) - 1):
                if temp == 100001:
                    temp = neww[j] - neww[j+1]
                    
                if temp != 100001 and neww[j] - neww[j+1] != temp:
                    isFalse = False
                    break
                    
                temp = neww[j] - neww[j+1]
                
            
            ans.append(isFalse)
            
            
        return ans
                
                