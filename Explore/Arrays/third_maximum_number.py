from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(dict.fromkeys(nums))
        if len(nums) < 3:
            return max(nums)
        first_max = -2147483648
        second_max = -2147483648
        third_max = -2147483648
        for num in nums:
            if first_max < num:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif first_max > num:
                if second_max < num:
                    third_max = second_max
                    second_max = num
                elif third_max < num:
                    third_max = num
        return third_max


sol = Solution()
arr = [3, 2, 1]
result = sol.thirdMax(arr)
print(result)
arr = [1, 2]
result = sol.thirdMax(arr)
print(result)
arr = [2, 2, 3, 1]
result = sol.thirdMax(arr)
print(result)
arr = [1, 1, 2]
result = sol.thirdMax(arr)
print(result)
arr = [1, 2, -2147483648]
result = sol.thirdMax(arr)
print(result)
