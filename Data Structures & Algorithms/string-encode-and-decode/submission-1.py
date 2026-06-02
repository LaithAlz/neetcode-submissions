class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            for char in string:
                ord_c = ord(char)
                new_c = ord_c * 3
                res += chr(new_c)
            res += "*"
        return res
            


    def decode(self, s: str) -> List[str]:
        res = []
        string = ""
        for char in s:
            if(char == "*"):
                res.append(string)
                string = ""
            else:
                new_c = ord(char)
                old_c = new_c // 3
                string += chr(old_c)
        return res