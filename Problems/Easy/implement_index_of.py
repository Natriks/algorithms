class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack) or needle not in haystack:
            return -1
        if needle == '':
            return 0
        return haystack.find(needle, 0)


sol = Solution()
print(sol.strStr('hello', 'll'))
print(sol.strStr('aaa', 'a'))
