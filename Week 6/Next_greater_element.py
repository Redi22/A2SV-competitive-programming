class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        lookup = {}
        result = []
        
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                temp = stack.pop()
                lookup[temp] = nums2[i]
                
            stack.append(nums2[i])
            lookup[nums2[i]] = -1
            
        for val in nums1:
            result.append(lookup[val])
            
        return result