class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        res = 0
        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]
            pre = currSum - k
            
            if pre in prefix:
                res += prefix[pre]
            
            if currSum in prefix:
                prefix[currSum] += 1
            else:
                prefix[currSum] = 1
        
        return res