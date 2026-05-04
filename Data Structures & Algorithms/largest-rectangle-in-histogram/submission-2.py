class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights) + 1):
            current_height = 0 if i == len(heights) else heights[i]
            while stack and heights[stack[-1]] > current_height:
                popped_bar = stack.pop()
                height = heights[popped_bar]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea
            