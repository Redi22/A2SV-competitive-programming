class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = [0]
        seen = defaultdict(int)
        ans = 0
        
        for num in nums:
            pref_sum.append(pref_sum[-1] + num)
            
        for summ in pref_sum:
            if summ - k in seen: 
                ans += seen[summ - k]
                
            seen[summ] += 1
        
        return ans