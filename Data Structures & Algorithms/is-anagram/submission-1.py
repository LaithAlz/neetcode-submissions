class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        if len(s) != len(t):
            return False

        
        for i in range(len(s)):
            letter_1 = s[i]
            letter_2 = t[i]

            if letter_1 not in freq1:
                freq1[letter_1] = 1
            else:
                freq1[letter_1] += 1

            if letter_2 not in freq2:
                freq2[letter_2] = 1
            else:
                freq2[letter_2] += 1
        
        return freq1 == freq2