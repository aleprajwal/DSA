# Linear search

"""
test case 1
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = 4

test case 2
nums = [-1, 0, 3, 5, 9, 12]
target = 2
result = -1
"""


class Solution(object):
    def search(self, nums, target):
        for index, num in enumerate(nums):
           if target == num:
               return index
        return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 2

solution = Solution()
result = solution.search(nums, target)

print(result)