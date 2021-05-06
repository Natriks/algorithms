from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = {}
        index = len(nums) - 1
        counter = 0
        while index >= 0:
            if nums[index] in pairs:
                pairs[nums[index]]['counter'] += pairs[nums[index]]['accumulator']
                pairs[nums[index]]['accumulator'] += 1
            else:
                pairs[nums[index]] = {'accumulator': 1, 'counter': 0}
            index -= 1
        for pair in pairs.values():
            counter += pair['counter']
        return counter


sol = Solution()
print(sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(sol.numIdenticalPairs([1, 1, 1, 1]))
assert sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
assert sol.numIdenticalPairs([1, 1, 1, 1]) == 6
assert sol.numIdenticalPairs([1, 2, 3]) == 0
