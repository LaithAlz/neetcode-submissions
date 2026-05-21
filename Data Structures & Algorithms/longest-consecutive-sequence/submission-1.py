class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no_dups = set()

        for num in nums:
            no_dups.add(num)
        longest = 0
        for num in nums:
            if num-1 not in no_dups:
                length = 1
                while num+length in no_dups:
                    length +=1 
                longest = max(length, longest)

        return longest
                
