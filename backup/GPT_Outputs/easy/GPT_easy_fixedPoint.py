# easy_fixedPoint.py

class LLM_Solution:
    def fixedPoint(self, arr):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                right = mid - 1  # keep searching for a smaller index to the left
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1

        return left if left < len(arr) and arr[left] == left else -1
