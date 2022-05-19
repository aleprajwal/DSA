class Solution():
    """
    Solve using hashmap concept
    complexity of this technique on this problem: O(n)
    first loop is linear traversal O(n), second uses hashmap O(1)
    
    testcase I:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
    testcase II:
    Input: nums = [-3,4,3,90], target = 0
    Output: [0, 2]
    """

    def twoSum(self, nums, target):
        look_up = dict()
        for i in range(0, len(nums)):
            search_num = target - nums[i]
            if search_num in look_up:
                return look_up[search_num], i
            look_up[nums[i]] = i


solution = Solution()
print(solution.__doc__)
result = solution.twoSum([3, 2, 4], 6)
print(result)