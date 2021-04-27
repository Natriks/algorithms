class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
        result = 0
        index = len(s) - 1
        next_roman_char = None
        while index >= 0:
            roman_char = s[index]
            if index != len(s) - 1:
                next_roman_char = s[index + 1]
            if next_roman_char and romans[roman_char] < romans[next_roman_char]:
                result -= romans[roman_char]
            else:
                result += romans[roman_char]
            index -= 1
        return result


sol = Solution()
assert sol.romanToInt("III") == 3
assert sol.romanToInt("IV") == 4
assert sol.romanToInt("IX") == 9
assert sol.romanToInt("LVIII") == 58
assert sol.romanToInt("MCMXCIV") == 1994
assert sol.romanToInt("MDCCCLXXXIV") == 1884
