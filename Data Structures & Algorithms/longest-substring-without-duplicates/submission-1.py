class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_size = 0

        distinct = set()
        while l <= r and r < len(s):
            if s[r] not in distinct:
                distinct.add(s[r])
                r += 1
            else:
                distinct.remove(s[l])
                l += 1
            size = r - l
            max_size = max(max_size, size)
            print(size, distinct)
        return max_size
