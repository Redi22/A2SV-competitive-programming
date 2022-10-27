class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        n = len(img1)
        
        # [1] first, we list coordinates (x,y) of 1-points in each image
        
        idx1 = [(i//n,i%n) for i in range(n**2) if img1[i//n][i%n]]
        idx2 = [(j//n,j%n) for j in range(n**2) if img2[j//n][j%n]]

        # [2] second, we obtain translation vectors (i1-j1, i2-j2) needed to
        #    overlap each 1-point of img1 with each 1-point of img2, and count
        #    frequencies of these vectors
        
        tr_vecs = Counter((i1-j1, i2-j2) for i1,i2 in idx1 for j1,j2 in idx2)
        
        # [3] translation vector that has been encountered most of the time is
        #    the one that produces an overlap of the maximal number of points
        
        return max(tr_vecs.values()) if tr_vecs else 0