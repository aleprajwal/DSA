
class Solution():
    """
    returns fibbonacci number of nth place

    Python3 implementation of Fibbonacci sequence
    Use of Recursion technique
    """

    def fibbonacci(self, n:int()):
        if n <= 2:
            return 1
        
        return self.fibbonacci(n-1) + self.fibbonacci(n-2)


if __name__ == "__main__":
    solution = Solution()
    n = 3
    result = solution.fibbonacci(n)

    print(result)