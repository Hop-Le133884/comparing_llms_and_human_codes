
import random
from math import sqrt
from bisect import bisect_left

class Solution:
    def repairCars(self, ranks, cars):
        def check(t):
            return sum(int(sqrt(t // r)) for r in ranks) >= cars

        return bisect_left(range(ranks[0] * cars * cars), True, key=check)


