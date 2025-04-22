import math
class LLM_Solution:
    def nthMagicalNumber(self, n, a, b):
        MOD = 10**9 + 7
        def lcm(x, y):
            return x * y // math.gcd(x, y)
        
        L = lcm(a, b)
        left, right = 0, n * min(a, b)
        while left < right:
            mid = (left + right) // 2
            if mid // a + mid // b - mid // L < n:
                left = mid + 1
            else:
                right = mid
        return left % MOD