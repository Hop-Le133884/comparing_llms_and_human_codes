# hard_nthMagicalNumber.py

class LLM_Solution:
    def nthMagicalNumber(self, n, a, b):
        MOD = 10**9 + 7

        # Helper function to calculate Least Common Multiple (LCM) of a and b
        def lcm(x, y):
            from math import gcd
            return x * y // gcd(x, y)

        # Binary search to find the nth magical number
        left, right = min(a, b), n * min(a, b)
        lcm_ab = lcm(a, b)

        while left < right:
            mid = (left + right) // 2
            if mid // a + mid // b - mid // lcm_ab >= n:
                right = mid
            else:
                left = mid + 1

        return left % MOD
