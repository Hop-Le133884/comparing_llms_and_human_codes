# hard_nthMagicalNumber.py

class LLM_Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """
        Nth Magical Number
        """
        MOD = 10**9 + 7

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        lcm = a * b // gcd(a, b)

        left, right = min(a, b), n * min(a, b)
        while left < right:
            mid = (left + right) // 2
            count = mid // a + mid // b - mid // lcm
            if count < n:
                left = mid + 1
            else:
                right = mid
        return left % MOD