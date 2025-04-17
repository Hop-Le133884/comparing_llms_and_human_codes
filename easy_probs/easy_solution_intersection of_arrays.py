
import random

class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        cnt = Counter(arr1 + arr2 + arr3)
        return [x for x in arr1 if cnt[x] == 3]

