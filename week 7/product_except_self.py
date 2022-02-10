class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fproduct = [1]
        bproduct = [1]
        product = 1
        result = []
        # for i in range(len(nums)):
        #     product *= nums[i]
        #     fproduct.append(product)
        # product = 1
        for i in range(len(nums)-1,0,-1):
            product *= nums[i]
            bproduct.append(product)
        product = 1  
        for i in range(len(nums)): 
            result.append(product*bproduct.pop())
            product *= nums[i]
           
        return result
        