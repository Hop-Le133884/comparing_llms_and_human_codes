# hard_maximizeSweetness.py

class LLM_Solution:
    def maximizeSweetness(self, sweetness, k):
        def canDivide(minSweetness):
            count, currentSweetness = 0, 0
            for s in sweetness:
                currentSweetness += s
                if currentSweetness >= minSweetness:
                    count += 1
                    currentSweetness = 0
            return count >= k + 1

        left, right = min(sweetness), sum(sweetness)
        
        while left < right:
            mid = (left + right + 1) // 2  # We are looking for the maximum possible sweetness
            if canDivide(mid):
                left = mid  # If we can divide, try for a larger sweetness
            else:
                right = mid - 1  # Otherwise, reduce the sweetness
        
        return left
