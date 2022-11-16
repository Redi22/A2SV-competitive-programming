# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 1
        higher = n
        
        while lower <= higher:
            mid = lower + (higher - lower) // 2
            
            if guess(mid) == -1:
                higher = mid - 1
            elif guess(mid) == 1:
                lower = mid + 1
            else:
                return mid
       