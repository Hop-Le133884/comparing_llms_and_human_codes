class LLM_Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        Find Peak Element

        A peak element is an element that is strictly greater than its neighbors.
        Given a 0-indexed integer array nums, find a peak element, and return its index.
        If the array contains multiple peaks, return the index to any of the peaks.
        You may imagine that nums[-1] = nums[n] = -∞.
        You must write an algorithm that runs in O(log n) time.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left