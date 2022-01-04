class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        sortedarr = [0]*n
        odd = 1
        even = 0
        if (n%2==0):
            mid = int(n/2)
        else:
            mid = n//2
        for i in range(mid):
            sortedarr[odd] = nums[i]
            odd += 2
        for i in range(mid,n):
            sortedarr[even] = nums[i] 
            even += 2
        return sortedarr