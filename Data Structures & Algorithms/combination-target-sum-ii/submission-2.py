class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        paths = []
        candidates.sort()
        def backtrack(path, j):
            if sum(path) > target:
                return
            if sum(path) == target:
                paths.append(path[::])
                return
            for i in range(j, len(candidates)):
                candidate = candidates[i]
                if i > j and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidate)
                backtrack(path, i+1)
                path.pop()
            
        
        backtrack([], 0)
        return paths



            
