class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(idx, pathSum ,path):
            if pathSum == target:
                result.append(path)
                return
            if pathSum > target:
                return
            
            for i in range(idx, len(candidates)):
                # path.append(candidates[i])
                backtrack(i, pathSum + candidates[i] ,path + [candidates[i]])
                # path.pop()
                
        backtrack(0,0, [])
        return result