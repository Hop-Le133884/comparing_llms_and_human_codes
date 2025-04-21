class LLM_Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Find Minimum in Rotated Sorted Array

        Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
        Given the sorted rotated array nums of unique elements, return the minimum element of this array.
        You must write an algorithm that runs in O(log n) time.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]