class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_index = 0
        right_index = len(heights) -1
        max = 0
        while left_index < right_index:

            area = min(heights[left_index], heights[right_index])  \
            *(right_index - left_index)

            if area > max:
                max = area
            if heights[left_index] < heights[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return max
            

        