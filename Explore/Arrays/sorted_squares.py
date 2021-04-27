from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    first_positive_index = 0
    for i in range(len(nums) - 1):
        if nums[i] >= 0:
            first_positive_index = i
        break
    negative_arr = nums[:first_positive_index]
    positive_arr = nums[first_positive_index:]

    negative_squares = list(map(lambda x: x*x, negative_arr))
    positive_squares = list(map(lambda x: x*x, positive_arr))
    negative_squares.extend(positive_squares)

    left = 0
    right = len(negative_squares) - 1
    result = []
    while left != right:
        if negative_squares[left] >= negative_squares[right]:
            result.append(negative_squares[left])
            left += 1
        else:
            result.append(negative_squares[right])
            right -= 1
    result.append(negative_squares[left])
    result.reverse()
    return result

result = sortedSquares([-4,-1,0,3,10])
print(result)
