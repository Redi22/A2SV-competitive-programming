class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def backtrack(candidates, pathSum ,path):
            if pathSum > target:
                return 
            
            if pathSum == target:
                result.append(path)
                return
                
            
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                backtrack(candidates[i+1:], pathSum + candidates[i] ,path + [candidates[i]])
                
        backtrack(candidates, 0, [])
        return result