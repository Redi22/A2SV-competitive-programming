class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        pref = [0]
        lookup = {0: -1}
        needed = sum(nums) % p
        count = len(nums)
        
        for num in nums:
            pref.append(pref[-1] + num)
            
        for i in range(1, len(pref)):
            lookup[pref[i] % p] = i - 1
            
            if (pref[i] - needed) % p in lookup:
                count = min(count, i - lookup[(pref[i] - needed) % p] - 1)
                
        return count if count < len(nums) else -1