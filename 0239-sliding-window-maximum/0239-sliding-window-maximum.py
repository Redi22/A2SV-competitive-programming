class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        maximums = []
        l = 0
        for r in range(len(nums)):
            
            if not queue or queue[0][0] > nums[r]:
                while queue and queue[-1][0] < nums[r]:
                    queue.pop()
                    
                queue.append((nums[r], r))
            
            elif queue[0][0] <= nums[r]:
                queue = deque([(nums[r], r)])
                
            while r - l + 1 > k:
                if queue[0] == (nums[l], l):
                    queue.popleft()
                    
                l += 1
                
            if r - l + 1 == k:
                maximums.append(queue[0][0])
        
        return maximums