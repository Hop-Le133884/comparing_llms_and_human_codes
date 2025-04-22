
from typing import *
from bisect import *
from collections import *
from copy import *
from datetime import *
from heapq import *
from math import *
from re import *
from string import *
from random import *
from itertools import *
from functools import *
from operator import *

import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import itertools
import functools
import operator


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# hard_maximizeSweetness.py

class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        """
        Divide Chocolate
        """

        def can_divide(min_sweetness):
            pieces = 0
            current_sweetness = 0
            for s in sweetness:
                current_sweetness += s
                if current_sweetness >= min_sweetness:
                    pieces += 1
                    current_sweetness = 0
            return pieces >= k + 1

        left, right = min(sweetness), sum(sweetness) // (k + 1)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            if can_divide(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

solution=Solution()
assert solution.maximizeSweetness([41, 97, 80], 0) == 218
assert solution.maximizeSweetness([18, 19, 42, 64], 0) == 143
assert solution.maximizeSweetness([1, 48, 30, 72, 7], 1) == 79
assert solution.maximizeSweetness([42, 18, 31, 17, 97, 11, 80, 55], 1) == 146
assert solution.maximizeSweetness([84, 63], 1) == 63
assert solution.maximizeSweetness([31, 4, 92, 1, 94, 19, 29, 14, 88, 86], 3) == 86
assert solution.maximizeSweetness([14, 38, 98, 40, 91, 61, 82, 41, 32, 46], 6) == 46
assert solution.maximizeSweetness([44, 11, 26, 29, 21], 1) == 55
assert solution.maximizeSweetness([46, 56, 2, 31], 3) == 2
assert solution.maximizeSweetness([14, 32, 49, 95, 52, 98, 78, 77, 51], 8) == 14
assert solution.maximizeSweetness([57, 73, 41, 92, 51, 89], 2) == 130
assert solution.maximizeSweetness([18, 27, 72, 87, 88], 1) == 117
assert solution.maximizeSweetness([47, 79, 39, 41, 73], 4) == 39
assert solution.maximizeSweetness([48, 65, 57, 83, 68], 1) == 151
assert solution.maximizeSweetness([75, 24, 23, 26, 58, 92], 0) == 298
assert solution.maximizeSweetness([64], 0) == 64
assert solution.maximizeSweetness([9, 89, 10, 5, 23, 52, 1, 33], 7) == 1
assert solution.maximizeSweetness([6, 11, 44, 28, 77, 78, 23], 6) == 6
assert solution.maximizeSweetness([21, 47], 1) == 21
assert solution.maximizeSweetness([56, 58, 21, 26, 71, 76, 68, 14, 64], 2) == 146
assert solution.maximizeSweetness([68, 29, 78], 0) == 175
assert solution.maximizeSweetness([41, 72, 21, 35, 46, 45, 51], 4) == 45
assert solution.maximizeSweetness([35, 64, 86, 48, 96, 10, 72, 66, 81, 28], 1) == 257
assert solution.maximizeSweetness([54, 15, 58, 42], 1) == 69
assert solution.maximizeSweetness([8, 45, 51, 6, 60, 25, 30], 1) == 110
assert solution.maximizeSweetness([22, 24, 73, 79, 100, 96], 2) == 96
assert solution.maximizeSweetness([1, 65, 10], 0) == 76
assert solution.maximizeSweetness([73, 44, 79, 8, 33, 89, 71, 75], 5) == 44
assert solution.maximizeSweetness([63, 10, 64, 79], 3) == 10
assert solution.maximizeSweetness([42, 62, 49], 1) == 49
assert solution.maximizeSweetness([62, 9, 32, 63, 64, 3, 81, 40, 98, 52], 7) == 40
assert solution.maximizeSweetness([66, 82, 10, 52, 48, 100, 96], 5) == 48
assert solution.maximizeSweetness([99, 68, 30, 24, 12, 17, 100, 92, 3], 3) == 95
assert solution.maximizeSweetness([29, 65, 26, 38, 30, 58, 1, 67, 72, 49], 2) == 121
assert solution.maximizeSweetness([47, 28, 77, 64], 2) == 64
assert solution.maximizeSweetness([3], 0) == 3
assert solution.maximizeSweetness([81, 2, 99, 18, 100], 3) == 18
assert solution.maximizeSweetness([73, 9, 80, 7, 24], 4) == 7
assert solution.maximizeSweetness([25, 11, 41, 32, 50, 29, 30, 57], 7) == 11
assert solution.maximizeSweetness([37], 0) == 37
assert solution.maximizeSweetness([17, 36, 44, 82, 35, 23, 8, 88, 77, 76], 2) == 153
assert solution.maximizeSweetness([57], 0) == 57
assert solution.maximizeSweetness([66, 58], 0) == 124
assert solution.maximizeSweetness([61, 46, 67, 64], 1) == 107
assert solution.maximizeSweetness([97, 76, 69, 28, 51], 2) == 79
assert solution.maximizeSweetness([14], 0) == 14
assert solution.maximizeSweetness([47, 2, 94, 96, 84, 74], 2) == 96
assert solution.maximizeSweetness([44], 0) == 44
assert solution.maximizeSweetness([55, 20], 0) == 75
assert solution.maximizeSweetness([76, 50, 93, 57, 92, 42, 5, 84], 0) == 499
assert solution.maximizeSweetness([10, 79, 3, 17, 77, 31, 42, 95], 6) == 10
assert solution.maximizeSweetness([89, 64, 80, 68, 57, 12, 62, 86, 56], 4) == 74
assert solution.maximizeSweetness([17, 78, 38], 1) == 38
assert solution.maximizeSweetness([52], 0) == 52
assert solution.maximizeSweetness([73, 4, 29, 61, 74, 26, 42, 83, 16], 1) == 167
assert solution.maximizeSweetness([11, 29, 60, 9, 43, 61, 49, 16, 31], 8) == 9
assert solution.maximizeSweetness([52, 24, 33, 16, 11, 53], 1) == 80
assert solution.maximizeSweetness([22, 56, 73, 43, 100, 84, 4, 52, 40, 91], 1) == 271
assert solution.maximizeSweetness([20, 62, 19, 21, 61, 10], 1) == 92
assert solution.maximizeSweetness([87, 13], 1) == 13
assert solution.maximizeSweetness([49, 40, 48, 37], 3) == 37
assert solution.maximizeSweetness([6, 70, 41, 51, 10, 47, 31, 94], 6) == 10
assert solution.maximizeSweetness([53, 92, 27, 100, 94, 32, 63], 3) == 94
assert solution.maximizeSweetness([84, 88], 0) == 172
assert solution.maximizeSweetness([81, 41, 51], 0) == 173
assert solution.maximizeSweetness([89, 37, 49, 98, 79, 32, 66, 10, 72], 1) == 259
assert solution.maximizeSweetness([84, 24, 96, 36, 8], 2) == 44
assert solution.maximizeSweetness([73], 0) == 73
assert solution.maximizeSweetness([86, 24, 63, 57], 3) == 24
assert solution.maximizeSweetness([9, 1, 73, 43, 31, 78, 80, 77, 70, 4], 0) == 466
assert solution.maximizeSweetness([6], 0) == 6
assert solution.maximizeSweetness([72, 23, 79], 1) == 79
assert solution.maximizeSweetness([41, 95, 100, 98, 37, 39, 24, 40, 78], 4) == 98
assert solution.maximizeSweetness([30, 61], 1) == 30
assert solution.maximizeSweetness([97, 8, 37, 46, 74], 2) == 74
assert solution.maximizeSweetness([37, 9], 0) == 46
assert solution.maximizeSweetness([56, 24, 31, 27], 2) == 27
assert solution.maximizeSweetness([58, 6], 1) == 6
assert solution.maximizeSweetness([18, 65, 77, 38, 6, 42], 0) == 246
assert solution.maximizeSweetness([91, 40, 81, 56, 50, 78, 62, 82, 39], 3) == 128
assert solution.maximizeSweetness([80, 66, 83, 16, 34, 99, 95, 27, 12, 31], 3) == 99
assert solution.maximizeSweetness([95, 39, 56, 13, 36, 84, 83, 72, 61], 5) == 61
assert solution.maximizeSweetness([60, 44, 38, 14, 74, 47, 17, 11], 5) == 28
assert solution.maximizeSweetness([64, 26, 87, 37], 1) == 90
assert solution.maximizeSweetness([51, 7, 1, 55, 24], 0) == 138
assert solution.maximizeSweetness([96, 12, 70, 3, 2], 3) == 5
assert solution.maximizeSweetness([65, 95, 6], 2) == 6
assert solution.maximizeSweetness([56, 75, 41, 94, 68, 59, 29, 14, 66], 2) == 162
assert solution.maximizeSweetness([91, 96, 17, 6, 18, 27, 56, 47], 3) == 68
assert solution.maximizeSweetness([82, 84, 10, 38, 5, 29, 88, 98], 6) == 10
assert solution.maximizeSweetness([10, 59, 20, 46], 1) == 66
assert solution.maximizeSweetness([44, 63, 54, 48, 71, 73, 20, 96], 3) == 102
assert solution.maximizeSweetness([53, 81, 89], 1) == 89
assert solution.maximizeSweetness([33, 29, 11], 1) == 33
assert solution.maximizeSweetness([23], 0) == 23
assert solution.maximizeSweetness([1], 0) == 1
assert solution.maximizeSweetness([45, 67, 91], 2) == 45
assert solution.maximizeSweetness([81, 59, 73, 22, 63], 3) == 59
assert solution.maximizeSweetness([35, 7, 18, 64, 20, 6, 40, 62, 98], 3) == 62
assert solution.maximizeSweetness([82, 50, 16, 52, 96, 95, 12, 1], 6) == 13