class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soliderDict = []
        for i in range(len(mat)):
            l = 0 
            r = len(mat[i]) - 1
            farIndex = -1
            while l <= r:
                mid = (l + r) // 2
                if mat[i][mid] == 1:
                    farIndex = mid
                    l = mid + 1
                else:
                    r = mid - 1
            soliderDict.append([ farIndex + 1 , i])
        soliderDict.sort()
        soliderDict = [i[1] for i in soliderDict]
        return soliderDict[:k]