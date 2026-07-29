class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = -1
        start = 0
        end = len(heights) - 1
        while start < end:
            ans = max(ans, (end - start) * min(heights[start], heights[end]))
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return ans
