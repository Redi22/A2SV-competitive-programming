class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_positions = {stone: index for index, stone in enumerate(stones)}
        
        @lru_cache(None)
        def dp(i, jump):
            if i >= len(stones):
                return False
            
            if i == len(stones) - 1:
                return True
        
            for k in [1, 0, -1]:
                new_index = stones[i] + jump + k
                if new_index in stone_positions and stone_positions[new_index] > i:
                    if dp(stone_positions[new_index], jump + k):
                        return True
                
            return False
            
        return dp(0, 0) 