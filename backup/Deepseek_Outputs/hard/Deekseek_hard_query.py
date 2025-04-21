import bisect
from collections import defaultdict
import random

class LLM_Solution:
    def __init__(self, arr):
        self.loc = defaultdict(list)
        for i, num in enumerate(arr):
            self.loc[num].append(i)
        self.arr = arr
        
    def query(self, left, right, threshold):
        length = right - left + 1
        for _ in range(20):
            idx = random.randint(left, right)
            num = self.arr[idx]
            lst = self.loc[num]
            l = bisect.bisect_left(lst, left)
            r = bisect.bisect_right(lst, right)
            if r - l >= threshold:
                return num
        return -1