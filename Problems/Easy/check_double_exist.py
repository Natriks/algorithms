from typing import List


class Solution:
    # def checkIfExist(self, arr: List[int]) -> bool:
    #     doubles = {}
    #     for num in arr:
    #         if num in doubles and doubles[num] != num:
    #             print(doubles)
    #             return True
    #         doubles[num * 2] = num
    #     print(doubles)
    #     return False

    def checkIfExist(self, arr: List[int]) -> bool:
        doubles = {}
        for num in arr:
            if num in doubles:
                print(doubles)
                return True
            doubles[num * 2] = num

        for num in arr:
            if num in doubles and doubles[num] != num:
                print(doubles)
                return True
        print(doubles)
        return False


sol = Solution()
# arr = [10, 2, 5, 3]
# arr = [7, 1, 14, 11]
arr = [-2, 0, 10, -19, 4, 6, -8]
result = sol.checkIfExist(arr)
print(result)
