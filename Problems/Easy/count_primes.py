class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        arr = [True for i in range(n)]
        arr[0] = False
        arr[1] = False

        for i in range(n):
            if arr[i]:
                j = i
                index = j + j
                while index < n:
                    arr[index] = False
                    index += j
        return arr.count(True)


sol = Solution()
res = sol.countPrimes(13)
print(res)

# 2, 3, 5, 7, 11, 13
