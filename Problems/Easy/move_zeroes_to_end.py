from typing import List
import time


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums) - 1
        i = 0
        counter = 0
        while i < length:
            if nums[i] == 0:
                nums.pop(i)
                length -= 1
                counter += 1
                continue
            i += 1
        for i in range(counter):
            nums.append(0)


sol = Solution()
arr = [0, 1, 0, 3, 12]

start = time.perf_counter()

sol.moveZeroes(arr)

end = time.perf_counter()

assert arr == [1, 3, 12, 0, 0]

print('time', start - end)
