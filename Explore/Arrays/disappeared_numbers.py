from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_value = len(nums)
        index = 1
        result_dict = {}
        result = []

        while index <= max_value:
            result_dict[nums[index - 1]] = index
            index += 1

        index = 1

        while index <= max_value:
            if index not in result_dict:
                result.append(index)
            index += 1
        return result


sol = Solution()
arr = [4, 3, 2, 7, 8, 2, 3, 1]
result = sol.findDisappearedNumbers(arr)
print(result)
arr = [1, 1]
result = sol.findDisappearedNumbers(arr)
print(result)
