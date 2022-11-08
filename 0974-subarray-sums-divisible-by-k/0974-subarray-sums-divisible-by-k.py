class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = [0]
        lookup = defaultdict(int)
        count = 0
        
        for num in nums:
            pref.append(pref[-1] + num)
            
        for i in range(len(pref)):
            if pref[i] % k in lookup:
                count += lookup[pref[i] % k]
                
            lookup[pref[i] % k] += 1
            
        return count