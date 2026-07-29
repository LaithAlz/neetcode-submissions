class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(string):
            return string == string[::-1]

        best = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if isPalindrome(substring):
                    if len(substring) > len(best):
                        best = substring
        
        return best
