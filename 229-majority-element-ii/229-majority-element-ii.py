class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maxx = len(nums) / 3
        ans = []
        c = Counter(nums)
        
        for i,num in c.items():
            if num > maxx:
                ans.append(i)
                
        return ans