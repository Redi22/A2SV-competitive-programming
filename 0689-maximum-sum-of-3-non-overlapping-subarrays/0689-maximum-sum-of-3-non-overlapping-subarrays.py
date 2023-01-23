class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = defaultdict(int)
        current = [0]
        replace = {3:1, 2:2, 1:3}

        for i in range(len(nums)):
            current.append(current[-1] + nums[i])
            
            if i >= k:
                sums[i - k] = current[i] - current[i - k]
            
        sums[len(nums) - k] = current[-1] - current[len(nums) - k]
        
        @cache
        def dp(i, count):
            if i >= len(sums) or count == 0:
                return [0, 0, 0, 0]
            
            take = dp(i + k, count - 1)
            first = i if count == 3 else take[1]
            sec = i if count == 2 else take[2]
            third = i if count == 1 else take[3]
            
            take = (take[0] + sums[i], first, sec, third)
            skip = dp(i + 1, count)
            
            if take[0] != skip[0]:
                return take if take[0] > skip[0] else skip
            
            for i in range(1, 4):
                if take[i] != skip[i]:
                    return take if take[i] < skip[i] else skip
            
        return dp(0, 3)[1:]
            