class Solution:
    def reverse(self, x: int) -> int:
        if x <= 0:
            val = -int(str(abs(x))[::-1])
            if val < -2147483647 or val > 2147483647:
                return 0
            return val
        val = int(str(x)[::-1])
        if val < -2147483647 or val > 2147483647:
            return 0
        return val
