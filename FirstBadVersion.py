class Solution():
    """
    You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

    

    Example 1:

    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.

    Example 2:

    Input: n = 1, bad = 1
    Output: 1

    Source: leetcode
    """
    def __init__(self, n, bad) -> None:
        self.n = n
        self.bad = bad

    def isBadVersion(self, n: int) -> bool:
        if n >= self.bad:
            return True
        return False


    def firstBadVersion(self) -> int:
        left = 1
        right = self.n
        while left <= right:
            mid = (left + right)//2
            if self.isBadVersion(mid) == True and self.isBadVersion(mid-1) == False:
                return mid
            elif self.isBadVersion(mid) == False:
                left = mid
            else:
                right = mid
        
        return -1


solution = Solution(5, 2)   # initilize solution object with `n` i.e, version number, and `bad` i.e, starting bad version
result = solution.firstBadVersion()
print(result)

