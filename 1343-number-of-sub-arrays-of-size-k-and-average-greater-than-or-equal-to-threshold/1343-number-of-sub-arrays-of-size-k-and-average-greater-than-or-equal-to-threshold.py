class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ , count = 0, 0
        
        for i in range(0, k-1):
            summ += arr[i]
            
        for i in range(k-1, len(arr)):
            summ += arr[i]
            
            if summ // k >= threshold:
                count += 1
                
            summ -= arr[i - k + 1]
                
        return count
        