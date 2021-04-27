from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        is_increasing = True
        has_decreased = False
        has_increased = False
        index = 1

        while index < len(arr):
            if is_increasing and arr[index - 1] < arr[index]:
                has_increased = True
                index += 1
            else:
                is_increasing = False
                if arr[index - 1] > arr[index]:
                    index += 1
                    has_decreased = True
                else:
                    return False
        if has_increased and has_decreased:
            return True
        return False


sol = Solution()
arr = [2, 1]
assert sol.validMountainArray(arr) == False
arr = [3, 5, 5]
assert sol.validMountainArray(arr) == False
arr = [0, 3, 2, 1]
assert sol.validMountainArray(arr) == True
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert sol.validMountainArray(arr) == False
# result = sol.validMountainArray(arr)
# print(result)
