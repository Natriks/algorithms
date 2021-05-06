from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "".rfind
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for word in strs:
            while word.find(prefix) != 0:
                prefix = prefix[0: len(prefix) - 1]
                if prefix == '':
                    return ''
        return prefix


sol = Solution()
assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
