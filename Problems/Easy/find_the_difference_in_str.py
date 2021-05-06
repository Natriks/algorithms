class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        string = s + t
        result = 0
        for ch in string:
            result ^= ord(ch)
        return chr(result)
