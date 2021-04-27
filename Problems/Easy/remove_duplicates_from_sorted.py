from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 1
        length = len(nums)
        while i < length:
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                length -= 1
            else:
                i += 1
        return len(nums)

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     result = list(dict.fromkeys(nums))
    #     nums.clear()
    #     nums.extend(result)
    #     return len(nums)


sol = Solution()
arr = [0, 1, 2, 2, 3, 0, 4, 2]
sol.removeDuplicates(arr)
print(arr)
