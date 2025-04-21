class LLM_Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            # Ensure mid is always even so we can check pairs
            if mid % 2 == 1:
                mid -= 1
            
            # If mid and mid+1 are equal, the unique element is in the right half
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        
        return nums[left]
