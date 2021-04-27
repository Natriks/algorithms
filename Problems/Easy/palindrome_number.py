class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     if x < 10:
    #         return True
    #     before = x
    #     result = 0
    #     while True:
    #         val = before % 10
    #         if val > 0 or before != 0:
    #             result *= 10
    #             result += val
    #             before = int(before / 10)
    #         else:
    #             break
    #     return x == result

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     if x < 10:
    #         return True
    #     result = []
    #     while x >= 1:
    #         result.append(x % 10)
    #         x = int(x / 10)
    #     for i in range(math.floor(len(result) / 2)):
    #         if result[i] != result[len(result) - 1 - i]:
    #             return False
    #     return True
    #

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


sol = Solution()
a = 121
result = sol.isPalindrome(a)
print(result)
a = 1001
result = sol.isPalindrome(a)
print(result)
