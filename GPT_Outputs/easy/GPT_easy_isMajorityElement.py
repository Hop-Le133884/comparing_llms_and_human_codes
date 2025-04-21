# easy_isMajorityElement.py

class LLM_Solution:
    def isMajorityElement(self, nums, target):
        def find_first():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        first = find_first()
        if first + len(nums) // 2 < len(nums) and nums[first + len(nums) // 2] == target:
            return True
        return False
