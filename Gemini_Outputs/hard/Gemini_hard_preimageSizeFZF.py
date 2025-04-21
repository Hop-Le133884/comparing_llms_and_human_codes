# hard_preimageSizeFZF.py

class LLM_Solution:
    def preimageSizeFZF(self, k: int) -> int:
        """
        Preimage Size of Factorial Zeroes Function
        """

        def count_trailing_zeros(x):
            count = 0
            while x > 0:
                x //= 5
                count += x
            return count

        left, right = 0, 5 * (k + 1)

        while left < right:
            mid = (left + right) // 2
            zeros = count_trailing_zeros(mid)
            if zeros < k:
                left = mid + 1
            else:
                right = mid
        low = left

        left, right = 0, 5 * (k + 1)
        while left < right:
            mid = (left + right) // 2
            zeros = count_trailing_zeros(mid)
            if zeros <= k:
                left = mid + 1
            else:
                right = mid
        high = left - 1

        return max(0, high - low + 1)