
class Factorial():
    """Calculation of a factorial using recursion concept"""
    
    def factorials(self, n:int()):
        if n >= 0:
            if n == 0:
                return 1
            print('return {} * factorials({})'.format(n, n-1))
            return n * self.factorials(n-1)


factorial = Factorial()
result = factorial.factorials(8)

print(result)