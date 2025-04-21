# hard_minOperations.py

class LLM_Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Minimum Number of Operations to Make Array Continuous
        """
        n = len(nums)
        unique_nums = sorted(list(set(nums)))
        unique_len = len(unique_nums)
        max_len = 0
        left = 0
        for right in range(unique_len):
            while unique_nums[right] - unique_nums[left] >= n:
                left += 1
            max_len = max(max_len, right - left + 1)
        return n - max_len