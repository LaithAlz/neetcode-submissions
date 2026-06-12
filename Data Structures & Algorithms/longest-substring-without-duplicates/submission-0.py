class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        distinct = set()
        size = 0
        max_size = 0
        while r < len(s) and l <= r:
            left_char = s[l]
            right_char = s[r]
            if right_char not in distinct:
                distinct.add(right_char)
                size += 1
                r += 1
            else:
                distinct.remove(left_char)
                size -= 1
                l += 1
            max_size = max(max_size, size)
        return max_size
            
