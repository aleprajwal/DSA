
class Solution():
    """

    Given an integer x, return true if x is palindrome integer
    An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is a palindrome while 123 is not.

    Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    """

    def palindrome(self, num):
        if num < 0 or num % 10 == 0 and num != 0:
            return False

        """    
        list_num = [int(n) for n in (num)]
        mid_index = int(len(list_num)/2)

        if len(list_num) % 2 == 0:
            first_half_num = list_num[0:mid_index]
        else:
            first_half_num = list_num[0:mid_index + 1]
        
        second_half_num = list_num[mid_index:]
        second_half_num.reverse()
        """
        first_half_num = num
        second_half_num = 0

        while first_half_num > second_half_num :
            second_half_num = second_half_num * 10 + first_half_num % 10
            first_half_num = int(first_half_num/10)
        
        if first_half_num == second_half_num or first_half_num == int(second_half_num/10):
            return True
        
        return False


num = 1234321
solution = Solution()
result = solution.palindrome(num)

print(result)
