from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights.copy()
        sorted_heights.sort()
        length = len(heights)
        index = 0
        wrong_count = 0
        while index < length:
            if heights[index] != sorted_heights[index]:
                wrong_count += 1
            index += 1
        return wrong_count


sol = Solution()
arr = [1, 1, 4, 2, 1, 3]
result = sol.heightChecker(arr)
print(result)
arr = [5, 1, 2, 3, 4]
result = sol.heightChecker(arr)
print(result)
arr = [1, 2, 3, 4, 5]
result = sol.heightChecker(arr)
print(result)
