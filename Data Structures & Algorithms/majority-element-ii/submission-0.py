class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freqs = {}
        skip = set()
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
            count = freqs[num]
            if count > len(nums) // 3 and num not in skip:
                res.append(num)
                skip.add(num)
                
        
        return res