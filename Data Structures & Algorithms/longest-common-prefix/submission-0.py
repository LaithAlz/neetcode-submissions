class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        freq = {}
        for word in strs:
            for i in range(1,len(word)+1):
                letter = word[:i]
                if letter in freq:
                    freq[letter] += 1
                else:
                    freq[letter] = 1
        longest = ""
        largest_val = -1
        
        for prefix in freq.keys():
            print(prefix)
            if freq[prefix] == len(strs):
                if len(prefix) > len(longest):
                    longest = prefix
                

        return longest
