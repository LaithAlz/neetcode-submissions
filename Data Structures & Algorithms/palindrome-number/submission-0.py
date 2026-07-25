class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = len(str(x)) - 1

        l = 0
        r = n
        str_x = str(x)
        while l < r:
            if str_x[l] != str_x[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
                

            