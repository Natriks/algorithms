from typing import List


class Solution:
    # def replaceElements(self, arr: List[int]) -> List[int]:
    #     if arr:
    #         index = 0
    #         while index < len(arr):
    #             right_side = arr[index + 1:]
    #             if right_side:
    #                 arr[index] = max(right_side)
    #             index += 1
    #         arr[len(arr) - 1] = -1
    #         return arr
    #     else:
    #         return []

    # def replaceElements(self, arr: List[int]) -> List[int]:
    #     if arr:
    #         index = 0
    #         max_value = max(arr)
    #         while index < len(arr):
    #             if arr[index] < max_value:
    #                 arr[index] = max_value
    #             elif arr[index] == max_value:
    #                 right_side = arr[index + 1:]
    #                 if right_side:
    #                     arr[index] = max(right_side)
    #                 index += 1
    #         arr[len(arr) - 1] = -1
    #         return arr
    #     else:
    #         return []

    def replaceElements(self, arr: List[int]) -> List[int]:
        if arr:
            index = len(arr) - 1
            max_right = arr[index]
            while index >= 0:
                if max_right >= arr[index]:
                    arr[index] = max_right
                else:
                    arr[index], max_right = max_right, arr[index]
                index -= 1
            arr[len(arr) - 1] = -1
            return arr
        else:
            return []


sol = Solution()
arr = [17, 18, 5, 4, 6, 1]
result = sol.replaceElements(arr)
arr = [17, 18, 5, 4, 6, 1]
print(result)
assert sol.replaceElements(arr) == [18, 6, 6, 6, 1, -1]
arr = [400]
assert sol.replaceElements(arr) == [-1]
arr = []
assert sol.replaceElements(arr) == []
# result = sol.validMountainArray(arr)
# print(result)
