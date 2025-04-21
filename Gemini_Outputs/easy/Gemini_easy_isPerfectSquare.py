# easy_isPerfectSquare.py

class LLM_Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Given a positive integer num, return true if num is a perfect square or false otherwise.
        A perfect square is an integer that is the square of an integer.
        You must not use any built-in library function, such as sqrt.
        """

        if num == 1:
            return True

        left, right = 1, num // 2

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False