class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxArea = 0

        # look through the area
        for i in range(len(heights) + 1):
            current_height = 0 if i == len(heights) else heights[i]
            while stk and heights[stk[-1]] > current_height:
                popped_bar = stk.pop()
                height = heights[popped_bar]
                width = i if not stk else i - stk[-1] - 1
                maxArea = max(maxArea, width * height)
            stk.append(i)
        return maxArea