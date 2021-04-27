from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                nums.remove(nums[i])
                length -= 1
            else:
                i += 1
        return len(nums)


sol = Solution()
arr = [0, 1, 2, 2, 3, 0, 4, 2]
sol.removeElement(arr, 2)
print(arr)
