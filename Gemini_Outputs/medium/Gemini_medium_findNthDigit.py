class LLM_Solution:
    def findNthDigit(self, n: int) -> int:
        """
        Nth Digit

        Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
        """
        digit_length = 1
        count = 9
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10

        start_num = 10 ** (digit_length - 1)
        num = start_num + (n - 1) // digit_length
        index_from_right = (n - 1) % digit_length
        return int(str(num)[index_from_right])