from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    index = 0
    length = len(arr)
    result = []
    while index < length:
        if arr[index] == 0:
            result.append(0)
        result.append(arr[index])
        index += 1
    arr.clear()
    arr.extend(result[:length])

ara = [1, 0, 2, 3, 0, 4, 5, 0]
# ara = [1, 2, 3]
duplicateZeros(ara)
print(ara)
