class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            nums2.append(nums1[i])
            
        for i in range(len(nums2)):
            nums1[i] = nums2[i]
        
        nums1.sort()
        