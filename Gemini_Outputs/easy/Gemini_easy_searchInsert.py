# easy_searchInsert.py

class LLM_Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.
        You must write an algorithm with O(log n) runtime complexity.
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left