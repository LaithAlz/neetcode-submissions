class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}': '{', ')': '(', ']': '['}

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif stack.pop() != pairs[char]:
                    return False
        
        return not stack

            
            