
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

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans, j = n, 0
        for i, v in enumerate(nums):
            while j < len(nums) and nums[j] - v <= n - 1:
                j += 1
            ans = min(ans, n - (j - i))
        return ans

solution=Solution()
assert solution.minOperations([35, 62]) == 1
assert solution.minOperations([7, 1, 49]) == 2
assert solution.minOperations([18, 22, 71]) == 2
assert solution.minOperations([9, 90, 34, 55, 84, 57, 35, 98, 81]) == 7
assert solution.minOperations([88, 59, 66, 75, 84]) == 3
assert solution.minOperations([72, 65, 31, 86, 48, 15, 13, 61, 92, 47]) == 8
assert solution.minOperations([86, 52, 37, 33, 99, 67]) == 4
assert solution.minOperations([95, 84, 52, 70, 9]) == 4
assert solution.minOperations([14, 27, 88, 49, 80, 24, 2, 39, 71]) == 7
assert solution.minOperations([95, 74, 83, 46, 86, 7, 67]) == 5
assert solution.minOperations([86, 14, 53, 73, 21, 46]) == 5
assert solution.minOperations([43, 58, 34, 25, 78]) == 4
assert solution.minOperations([27, 2, 16, 98, 53, 25, 12, 72, 26, 73]) == 7
assert solution.minOperations([75, 16, 3]) == 2
assert solution.minOperations([68, 73, 20, 42, 5]) == 4
assert solution.minOperations([29, 82, 59]) == 2
assert solution.minOperations([44, 38, 2, 47, 30, 61, 52]) == 5
assert solution.minOperations([21, 14]) == 1
assert solution.minOperations([88, 10, 96, 38, 47]) == 4
assert solution.minOperations([92, 34, 69, 23, 73, 10]) == 4
assert solution.minOperations([65, 82]) == 1
assert solution.minOperations([2, 25, 81, 22, 84]) == 3
assert solution.minOperations([47, 97, 41, 75, 67, 92, 95, 13, 10, 26]) == 7
assert solution.minOperations([41, 80, 14, 12, 18, 99, 93, 20, 22]) == 5
assert solution.minOperations([85, 16, 66, 77, 41, 10, 33, 96, 81]) == 6
assert solution.minOperations([90, 54, 21, 83, 55, 62, 69, 65]) == 5
assert solution.minOperations([30, 70, 14, 44, 95, 51, 47]) == 5
assert solution.minOperations([61, 86, 79, 41, 96, 47, 4]) == 5
assert solution.minOperations([60, 10, 72]) == 2
assert solution.minOperations([50, 17, 44, 71, 80, 46]) == 4
assert solution.minOperations([16, 62, 82, 57, 85, 13, 20, 6]) == 5
assert solution.minOperations([88, 37, 52, 57, 36]) == 3
assert solution.minOperations([54, 9, 6, 65, 20, 37]) == 4
assert solution.minOperations([19, 95, 86, 40, 75]) == 4
assert solution.minOperations([20, 16, 52, 73, 97, 90, 68, 57, 2, 15]) == 7
assert solution.minOperations([4, 39, 36, 77, 96]) == 3
assert solution.minOperations([69, 52, 21, 71, 55]) == 3
assert solution.minOperations([72, 60, 77, 15, 3, 23, 5]) == 5
assert solution.minOperations([73, 47, 87, 69]) == 3
assert solution.minOperations([86, 23, 10, 98, 90, 15, 95]) == 5
assert solution.minOperations([11, 15, 42, 96]) == 3
assert solution.minOperations([55, 99, 59, 90, 29, 37, 81]) == 5
assert solution.minOperations([30, 70, 76, 73, 16, 48]) == 4
assert solution.minOperations([17, 25]) == 1
assert solution.minOperations([4, 28, 3, 95, 59, 34]) == 4
assert solution.minOperations([90, 67, 9, 1, 38, 52, 70]) == 5
assert solution.minOperations([46, 99, 9, 47, 7]) == 3
assert solution.minOperations([76, 93, 57, 11, 67, 22, 28]) == 5
assert solution.minOperations([35, 38, 90, 54]) == 2
assert solution.minOperations([54, 69, 47, 22, 7, 26, 2, 19]) == 5
assert solution.minOperations([57, 42, 40, 91, 55, 29]) == 4
assert solution.minOperations([97, 95, 85, 42, 86, 10, 66, 73]) == 6
assert solution.minOperations([90, 77, 97, 99]) == 2
assert solution.minOperations([70, 30, 96, 18, 29, 4]) == 4
assert solution.minOperations([70, 40, 99, 23, 53, 100, 82, 13]) == 6
assert solution.minOperations([38, 77, 87, 13, 98, 27, 50]) == 6
assert solution.minOperations([69, 28]) == 1
assert solution.minOperations([57, 74, 39, 38, 93]) == 3
assert solution.minOperations([43, 70, 39, 1, 72]) == 3
assert solution.minOperations([48, 62, 60, 64, 68, 52, 56]) == 4
assert solution.minOperations([23, 41, 83, 8, 43, 73, 86]) == 5
assert solution.minOperations([96, 86, 4, 9, 44, 14, 28, 69, 97, 11]) == 7
assert solution.minOperations([39, 72, 56, 13, 99, 87, 54, 40, 84, 49]) == 7
assert solution.minOperations([72, 41, 10, 21, 33, 46]) == 4
assert solution.minOperations([62, 75, 54, 86, 41, 17]) == 5
assert solution.minOperations([50, 95]) == 1
assert solution.minOperations([9, 3, 78, 63, 16]) == 4
assert solution.minOperations([90, 95, 22, 64, 25, 1, 49]) == 5
assert solution.minOperations([76, 99, 68, 45, 22]) == 4
assert solution.minOperations([63, 51, 19, 81]) == 3
assert solution.minOperations([50, 69, 71, 86]) == 2
assert solution.minOperations([18, 99]) == 1
assert solution.minOperations([91, 34, 81, 83, 66, 26, 11]) == 5
assert solution.minOperations([71, 100, 54, 36]) == 3
assert solution.minOperations([88, 66, 30, 39, 43, 97, 69, 5]) == 6
assert solution.minOperations([37, 6, 33, 88, 22, 74, 92, 8]) == 6
assert solution.minOperations([19, 3, 47, 89]) == 3
assert solution.minOperations([92, 6, 52]) == 2
assert solution.minOperations([67, 68, 55, 10, 23, 79]) == 4
assert solution.minOperations([22, 78, 39]) == 2
assert solution.minOperations([92, 1, 51, 52, 2]) == 3
assert solution.minOperations([5, 6, 45, 96, 53, 32, 89, 42, 74]) == 7
assert solution.minOperations([42, 95, 28, 46, 85]) == 3
assert solution.minOperations([15, 27, 5, 12, 19, 9, 3]) == 4
assert solution.minOperations([49, 68, 43, 29, 90, 45, 24, 52]) == 5
assert solution.minOperations([51, 77, 60, 29, 20, 71, 13]) == 5
assert solution.minOperations([16, 48]) == 1
assert solution.minOperations([8, 32]) == 1
assert solution.minOperations([61, 92]) == 1
assert solution.minOperations([46, 97, 13, 14, 48, 28, 20, 87]) == 5
assert solution.minOperations([40, 25, 52, 95, 65, 92]) == 4
assert solution.minOperations([98, 30, 89, 22, 97, 19, 31, 23, 42]) == 6
assert solution.minOperations([41, 48, 31, 77, 58]) == 4
assert solution.minOperations([15, 12, 90, 40, 34, 39, 87, 6]) == 5
assert solution.minOperations([22, 34, 28, 64, 92, 15, 18, 7, 77]) == 6
assert solution.minOperations([30, 75, 94]) == 2
assert solution.minOperations([81, 73, 98, 40, 53, 90, 28]) == 6
assert solution.minOperations([68, 17, 33, 75, 60, 52, 26]) == 6
assert solution.minOperations([1, 39, 70, 32, 45, 3, 71, 77]) == 5
assert solution.minOperations([59, 29, 93, 25, 87]) == 3