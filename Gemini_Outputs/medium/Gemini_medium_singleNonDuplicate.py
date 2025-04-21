class LLM_Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        Single Element in a Sorted Array

        You are given a sorted array consisting of only integers where every element appears exactly twice,
        except for one element which appears exactly once.
        Return the single element that appears only once.
        Your solution must run in O(log n) time and O(1) space.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1  # Ensure mid is even
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]