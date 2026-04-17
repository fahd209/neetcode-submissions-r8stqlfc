class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = float('-inf')
        L = 0
        R = len(heights) - 1

        while L < R:
            height = min(heights[L], heights[R])
            width = R - L
            max_water = max(max_water, width * height)

            if heights[L] < heights[R]:
                L += 1
            elif heights[L] > heights[R]:
                R -= 1
            else:
                R -= 1
                L += 1

        return max_water
        