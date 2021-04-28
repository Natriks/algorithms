class Solution:
    def isHappy(self, n: int) -> bool:
        summ = 0
        passed = set()
        while summ != 1:
            while n >= 1:
                    a = n % 10
                    summ += a * a
                    n = int(n / 10)
            if summ == 1:
                return True
            else:
                if summ in passed:
                    return False
                passed.add(summ)
                n = summ
                summ = 0
        return False

sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))
