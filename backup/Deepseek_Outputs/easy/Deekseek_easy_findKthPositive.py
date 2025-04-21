class LLM_Solution:
    def findKthPositive(self, arr, k):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        return left + k