
class Solution():
    """
    TestCase 1:

    Input: s = "III"
    Output: 3
    Explanation: III = 3.

    Example 2:

    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

    Example 3:

    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    Solution involves use of hashmap/table concept 
    Time complexity of the solution O(n) 

    Roman to Integer/Decimal
    if small value preceed before large subtract else add
    s = "MCMXCIV" = 1000 - 100 + 1000 - 10 + 100 - 1 + 5 = 1994
    """
    
    def romanToInteger(self, s):    
        roman_symbol = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        sum = 0
        for i in range(0, len(s)):
            if i+1 < len(s) and roman_symbol[s[i]] < roman_symbol[s[i+1]]:
                sum -= roman_symbol[s[i]]
                            
            else:
                sum += roman_symbol[s[i]] 

        return sum


roman = "MCMXCIV"
solution = Solution()
result = solution.romanToInteger(roman)

print(solution.__doc__)
print(result)
    