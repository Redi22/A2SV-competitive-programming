class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negPt = [n for n in nums if n < 0]
        posPt = [n for n in nums if n > 0]
        
        arr = []
        ng = 0
        po = 0
        while len(arr) < len(nums):
            arr.append(posPt[ng])
            arr.append(negPt[po])
            ng += 1
            po += 1
            
        return arr
            