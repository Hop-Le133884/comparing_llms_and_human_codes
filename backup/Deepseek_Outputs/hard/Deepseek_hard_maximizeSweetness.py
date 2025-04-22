class LLM_Solution:
    def maximizeSweetness(self, sweetness, k):
        left, right = min(sweetness), sum(sweetness)
        while left < right:
            mid = (left + right + 1) // 2
            current_sum = 0
            pieces = 0
            for s in sweetness:
                current_sum += s
                if current_sum >= mid:
                    pieces += 1
                    current_sum = 0
            if pieces >= k + 1:
                left = mid
            else:
                right = mid - 1
        return left