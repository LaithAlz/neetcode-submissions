class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        current = 0
        minLen = 100000000
        for r in range(len(nums)):
            current += nums[r]

            while current >= target:
                if current >= target:
                    minLen = min(minLen, r - l + 1)
                current -= nums[l]
                l += 1

        return 0 if minLen == 100000000 else minLen
