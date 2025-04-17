
import random

class Solution:
    def isMajorityElement(self, nums, target):
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return right - left > len(nums) // 2

