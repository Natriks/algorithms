from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        passed = set()
        for num in nums:
            if num in passed:
                return num
            passed.add(num)

    # def findDuplicate(self, nums: List[int]) -> int:
    #     for num in nums:
    #         if nums.count(num) > 1:
    #             return num

    # def findDuplicate(self, nums: List[int]) -> int:
    #     passed = set()
    #     left = 0
    #     right = len(nums) - 1
    #     while left <= right:
    #         if nums[left] in passed:
    #             return nums[left]
    #         else:
    #             passed.add(nums[left])
    #         left += 1
    #
    #         if nums[right] in passed:
    #             return nums[right]
    #         else:
    #             passed.add(nums[right])
    #         right -= 1
    #     return 0


sol = Solution()
arr = [1, 3, 4, 2, 2]
result = sol.findDuplicate(arr)
print(result)
arr = [3, 1, 3, 4, 2]
result = sol.findDuplicate(arr)
print(result)
arr = [1, 1]
result = sol.findDuplicate(arr)
print(result)
arr = [1, 1, 2]
result = sol.findDuplicate(arr)
print(result)
