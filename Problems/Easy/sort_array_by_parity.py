from typing import List
import time


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        length = len(nums)
        index = 0
        while index < length:
            if nums[index] % 2 == 0:
                result.append(nums.pop(index))
                length -= 1
                index -= 1
            index += 1
        result.extend(nums)
        return result


sol = Solution()
arr = [3, 1, 2, 4]

start = time.perf_counter()

arr = sol.sortArrayByParity(arr)

end = time.perf_counter()
print(arr)
assert arr == [2, 4, 3, 1]

print("time", start - end)
