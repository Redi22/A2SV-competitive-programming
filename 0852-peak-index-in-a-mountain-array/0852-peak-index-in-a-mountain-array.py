class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0 
        r = len(arr) - 1
        best = -1
        
        while l < r:
            mid = (r + l) // 2
            
            if arr[mid] < arr[mid - 1]:
                r = mid 
            else:
                best = mid
                l = mid + 1
                
        return best