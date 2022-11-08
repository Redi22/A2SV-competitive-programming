class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        sets = 0
        resets = 0
        shift = 0
        
        for num in nums:
            xor ^= num
        
        while xor & 1 == 0:
            xor = xor >> 1
            shift += 1
            
        for num in nums:
            if num & (1 << shift) == 0:
                resets ^= num
            else:
                sets ^= num

        return [sets, resets]
                
                
                
        