class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant_bloom = sorted(zip(growTime, plantTime), reverse=True)
        offset = 0
        max_time = float("-inf")
        for grow, plant in plant_bloom:
            max_time = max(max_time, grow + plant + offset)
            offset += plant
            
        return max_time
            