# easy_mySqrt.py

class LLM_Solution:
    def mySqrt(self, x: int) -> int:
        """
        Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
        The returned integer should be non-negative as well.
        You must not use any built-in exponent function or operator.
        """

        if x == 0:
            return 0

        left, right = 1, x
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            if mid <= x // mid:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result