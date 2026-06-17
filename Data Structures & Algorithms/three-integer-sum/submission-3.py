class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        for k in range(len(nums)):
            num_k = nums[k]
            l = k+1
            r = len(nums) - 1
            while l < r:
                num_l = nums[l]
                num_r = nums[r]
                total = num_k + num_l + num_r
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    if (num_l, num_k, num_r) not in seen:
                        res.append([num_l, num_k, num_r])
                        seen.add((num_l, num_k, num_r))
                    l += 1
        
        return res
