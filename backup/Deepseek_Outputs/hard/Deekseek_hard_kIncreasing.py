import bisect

class LLM_Solution:
    def kIncreasing(self, arr, k):
        def longest_non_decreasing_subsequence(nums):
            tails = []
            for num in nums:
                idx = bisect.bisect_right(tails, num)
                if idx == len(tails):
                    tails.append(num)
                else:
                    tails[idx] = num
            return len(tails)
        
        total_operations = 0
        for i in range(k):
            subarray = arr[i::k]
            lnds = longest_non_decreasing_subsequence(subarray)
            total_operations += len(subarray) - lnds
        return total_operations