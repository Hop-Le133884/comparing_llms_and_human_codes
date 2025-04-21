# easy_isMajorityElement.py

class LLM_Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        """
        Given an integer array nums sorted in non-decreasing order and an integer target,
        return true if target is a majority element, or false otherwise.
        A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.
        """

        count = 0
        for num in nums:
            if num == target:
                count += 1

        return count > len(nums) // 2