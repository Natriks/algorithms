from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            center = int(left + (right - left) / 2)
            if nums[center] == target:
                return center
            elif nums[center] > target:
                right = center - 1
            elif nums[center] < target:
                left = center + 1
        if nums[center] < target:
            return center + 1
        return center


sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 1))
