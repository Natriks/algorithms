from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        partial_sum = 0
        for num in nums:
            partial_sum += num
            max_sum = max(max_sum, partial_sum)
            if partial_sum < 0:
                partial_sum = 0
        return max_sum
