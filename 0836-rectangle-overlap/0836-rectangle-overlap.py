class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        intersection_1 = False
        intersection_2 = False
        
        if rec1[0] < rec2[2] and rec2[0] < rec1[2]:
            intersection_1 = True
            
        if rec2[1] < rec1[3] and rec1[1] < rec2[3]:
            intersection_2 = True
            
            
        return intersection_1 and intersection_2
    
    