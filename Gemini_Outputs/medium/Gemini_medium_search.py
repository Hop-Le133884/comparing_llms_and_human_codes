class LLM_Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """
        Search in Rotated Sorted Array II

        There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
        Given the array nums after the rotation and an integer target,
        return true if target is in nums, or false if it is not in nums.
        You must decrease the overall operation steps as much as possible.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False