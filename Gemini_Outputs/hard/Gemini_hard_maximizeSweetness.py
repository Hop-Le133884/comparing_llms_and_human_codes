# hard_maximizeSweetness.py

class LLM_Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        """
        Divide Chocolate
        """

        def can_divide(min_sweetness):
            pieces = 0
            current_sweetness = 0
            for s in sweetness:
                current_sweetness += s
                if current_sweetness >= min_sweetness:
                    pieces += 1
                    current_sweetness = 0
            return pieces >= k + 1

        left, right = min(sweetness), sum(sweetness) // (k + 1)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            if can_divide(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans