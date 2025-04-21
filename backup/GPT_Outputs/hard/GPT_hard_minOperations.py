# hard_minOperations.py

class LLM_Solution:
    def minOperations(self, nums):
        nums = list(set(nums))  # Remove duplicates
        nums.sort()  # Sort the unique elements

        n = len(nums)
        min_ops = n  # Initialize with the worst case (replace all elements)

        for i in range(n):
            # Find the smallest window of size n where the difference between max and min is n-1
            end = i + n - 1
            if end >= n:
                break
            min_ops = min(min_ops, nums[end] - nums[i] + 1 - n)

        return min_ops
