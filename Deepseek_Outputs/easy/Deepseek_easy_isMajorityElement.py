class LLM_Solution:
    def isMajorityElement(self, nums, target):
        def binary_search_left(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binary_search_right(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        left_idx = binary_search_left(nums, target)
        right_idx = binary_search_right(nums, target)
        count = right_idx - left_idx
        return count > len(nums) / 2