class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        def backtrack(start, path):
            if path not in res:
                res.append(path[::])
                

            for i in range(start, len(nums)):
                if start > i and nums[i] == num[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return res