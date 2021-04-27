from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for index in range(len(nums)):
            diff_map[target - nums[index]] = index

        for index in range(len(nums)):
            if nums[index] in diff_map and index != diff_map[nums[index]]:
                return [index, diff_map[nums[index]]]


sol = Solution()
assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert sol.twoSum([3, 2, 4], 6) == [1, 2]
assert sol.twoSum([3, 3], 6) == [0, 1]
