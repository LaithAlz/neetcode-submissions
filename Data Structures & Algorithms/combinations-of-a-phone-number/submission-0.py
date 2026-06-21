class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToChar = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res= []
        def backtrack(level_index, path):

            if len(path) == len(digits):
                res.append("".join(path[::]))
                return
            
            if len(path) > len(digits):
                return
            
            for char in numToChar[digits[level_index]]:
                path.append(char)
                backtrack(level_index + 1, path)
                path.pop()
        if len(digits) == 0:
            return []
        backtrack(0, [])
        return res




