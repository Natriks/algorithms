class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)[:1:-1]
        if len(a) < 32:
            a += '0' * (32 - len(a))
        return int(a, 2)


sol = Solution()
a = sol.reverseBits(43261596)
print(a)
