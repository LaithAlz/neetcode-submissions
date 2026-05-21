class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = i


        for i in range(len(nums)):
            num = nums[i]
            t = target - num
            if t in numbers and i != numbers[t]:
                return [i, numbers[target-num]]

     
            
