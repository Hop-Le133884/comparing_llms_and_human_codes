class LLM_Solution:
    def minOperations(self, nums):
        n = len(nums)
        unique_nums = sorted(list(set(nums)))
        res = float('inf')
        for i in range(len(unique_nums)):
            left = unique_nums[i]
            right = left + n - 1
            j = bisect.bisect_right(unique_nums, right)
            res = min(res, n - (j - i))
        return res