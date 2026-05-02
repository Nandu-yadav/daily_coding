def largestRectangleArea(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n):
        # Pop while current bar is smaller
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    # Process remaining bars
    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)

    return max_area


# Example
heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))
