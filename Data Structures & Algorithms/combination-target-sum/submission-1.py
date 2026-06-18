class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(i, path):
            if sum(path) == target and path not in res:
                res.append(path[::])
                return
            
            if sum(path) > target:
                return
            
            for i in range(i, len(nums)):
                path.append(nums[i])
                backtrack(i, path)
                path.pop()
            
        
        backtrack(0, [])
        return res