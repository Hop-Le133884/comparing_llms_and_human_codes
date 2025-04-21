# hard_findMin.py

class LLM_Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Find Minimum in Rotated Sorted Array II
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1  # Skip duplicate
        return nums[left]