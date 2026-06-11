class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        total = 0
        while l < r:
            left = heights[l]
            right = heights[r]

            commonHeight = min(left, right)
            area = commonHeight * (r - l)
            if left < right:
                l += 1
            if right <= left:
                r -= 1
            total = max(area, total)
        return total


