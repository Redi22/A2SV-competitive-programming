class Solution:
    def makeBouquets(self, day, bloomDay, k):
        count = 0
        i = 0
        j = 0
        while i < len(bloomDay) and j < len(bloomDay):
            if bloomDay[j] > day:
                i = j + 1
                
            if j - i + 1 == k:
                count += 1
                i = j + 1
                
            j += 1
            
        return count
        
    def search(self, r, bloomDay, k, required):
        l = 1
        best = -1
        while l <= r:
            mid_day = (r + l) // 2
            bouquets = self.makeBouquets(mid_day, bloomDay, k)
            if bouquets < required:
                l = mid_day + 1
            else:
                best = mid_day
                r = mid_day - 1
        return best
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        return self.search(max(bloomDay), bloomDay, k, m)