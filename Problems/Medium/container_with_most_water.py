from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_index = 0
        right_index = len(height) - 1
        while left_index < right_index:
            area = min(height[left_index], height[right_index]) * (right_index - left_index)
            if area > max_area:
                max_area = area
            if height[left_index] > height[right_index]:
                right_index -= 1
            else:
                left_index += 1
        return max_area


sol = Solution()
arr = [1, 1]
assert sol.maxArea(arr) == 1
arr = [4, 3, 2, 1, 4]
assert sol.maxArea(arr) == 16
arr = [1, 2, 1]
assert sol.maxArea(arr) == 2
