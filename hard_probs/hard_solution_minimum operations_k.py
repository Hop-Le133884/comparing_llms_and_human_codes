
import random

# Define the Solution class
class Solution:
    def kIncreasing(self, arr, k):
        def lis(arr):
            t = []
            for x in arr:
                idx = bisect_right(t, x)
                if idx == len(t):
                    t.append(x)
                else:
                    t[idx] = x
            return len(arr) - len(t)

        return sum(lis(arr[i::k]) for i in range(k))


