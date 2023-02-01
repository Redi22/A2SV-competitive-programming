class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_count = k
        count = 0
        count_w = 0
        l = 0
        for r in range(len(blocks)):
            count_w += (blocks[r] == "W")
            
            if r - l + 1 >= k:
                min_count = min(min_count, count_w)
                count_w -= (blocks[l] == "W")
                l += 1
            
        return min_count
        