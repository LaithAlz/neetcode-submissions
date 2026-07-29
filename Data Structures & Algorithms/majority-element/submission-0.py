class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = Counter(nums)

        for num, freq in freqs.items():
            if freq >= len(nums) // 2:
                return num