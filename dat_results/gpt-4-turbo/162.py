
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
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


solution=Solution()
assert solution.findPeakElement([11, 22, 35]) == 2
assert solution.findPeakElement([88, 84, 81, 57, 83, 96, 40, 80, 9]) == 7
assert solution.findPeakElement([57, 90, 85, 45, 51, 73]) == 1
assert solution.findPeakElement([100, 2, 40, 24, 8, 52, 64, 47, 80]) == 6
assert solution.findPeakElement([8, 66, 87, 23, 75, 19]) == 2
assert solution.findPeakElement([14, 95, 70, 13, 51, 35, 49, 59]) == 7
assert solution.findPeakElement([17, 63, 83, 9, 88, 21]) == 2
assert solution.findPeakElement([51, 48, 8, 31, 56, 10]) == 4
assert solution.findPeakElement([52, 87, 69, 59, 22, 38, 24, 47]) == 1
assert solution.findPeakElement([39, 16, 77, 93, 41, 91]) == 5
assert solution.findPeakElement([90, 95, 72, 49, 12, 2, 40, 20]) == 1
assert solution.findPeakElement([59, 92, 35, 72, 49, 95, 21, 26, 100, 52]) == 8
assert solution.findPeakElement([27, 49, 60, 56, 52, 68, 6]) == 2
assert solution.findPeakElement([16, 98, 19, 84, 60, 33, 24]) == 1
assert solution.findPeakElement([58, 51, 26, 93, 12, 46, 91, 88, 80]) == 6
assert solution.findPeakElement([31, 28, 1, 46, 92, 54]) == 4
assert solution.findPeakElement([52, 46, 48, 33]) == 2
assert solution.findPeakElement([56, 91, 3, 63, 100, 66]) == 4
assert solution.findPeakElement([67, 18, 23, 73, 2, 64, 48]) == 3
assert solution.findPeakElement([97, 35, 23, 7]) == 0
assert solution.findPeakElement([12, 20, 47, 77, 3, 41, 78, 94, 39]) == 7
assert solution.findPeakElement([78, 12]) == 0
assert solution.findPeakElement([37, 56, 92, 28]) == 2
assert solution.findPeakElement([89, 19, 92, 5, 77, 22, 18, 71, 23, 78]) == 2
assert solution.findPeakElement([58, 99]) == 1
assert solution.findPeakElement([88, 67, 63, 25, 66, 95, 37, 10, 35, 23]) == 8
assert solution.findPeakElement([65, 92, 77, 52, 53, 34, 87, 81]) == 6
assert solution.findPeakElement([50, 43, 56, 73, 80]) == 4
assert solution.findPeakElement([95, 43, 85, 66, 38, 50, 32, 37, 57, 8]) == 8
assert solution.findPeakElement([36, 44, 69, 33, 87]) == 2
assert solution.findPeakElement([19, 23, 97, 21, 58, 52, 71, 83, 54, 99]) == 2
assert solution.findPeakElement([52, 2, 49, 97, 25, 44, 45]) == 3
assert solution.findPeakElement([25, 81, 45, 99, 79, 93, 73, 71]) == 1
assert solution.findPeakElement([96, 49, 25, 32, 98]) == 4
assert solution.findPeakElement([99, 53, 75, 51, 13, 12, 56, 19]) == 2
assert solution.findPeakElement([27, 99]) == 1
assert solution.findPeakElement([67, 53, 82, 88, 33, 65, 6, 59]) == 3
assert solution.findPeakElement([74, 94]) == 1
assert solution.findPeakElement([59, 77, 33, 90, 52]) == 3
assert solution.findPeakElement([60, 56, 98]) == 2
assert solution.findPeakElement([49, 11, 82, 29, 22, 99, 46, 10, 85]) == 5
assert solution.findPeakElement([39, 25, 11]) == 0
assert solution.findPeakElement([56, 42, 30, 98, 23, 7, 40, 1, 94, 18]) == 3
assert solution.findPeakElement([19, 52, 24, 30, 12]) == 3
assert solution.findPeakElement([85, 21, 1, 88, 59, 14, 63, 68, 61, 90]) == 3
assert solution.findPeakElement([87, 49, 7, 83]) == 0
assert solution.findPeakElement([83, 82]) == 0
assert solution.findPeakElement([77, 43, 20, 56, 31]) == 3
assert solution.findPeakElement([68, 16, 31, 45, 13, 96, 52, 69, 67, 22]) == 7
assert solution.findPeakElement([67, 83]) == 1
assert solution.findPeakElement([61, 17, 96]) == 2
assert solution.findPeakElement([81, 49, 13, 95, 73, 46]) == 3
assert solution.findPeakElement([55, 47, 69, 94]) == 3
assert solution.findPeakElement([7, 36, 35, 99, 47]) == 3
assert solution.findPeakElement([85, 82, 2]) == 0
assert solution.findPeakElement([23, 78, 100, 50, 25, 41, 89, 13]) == 2
assert solution.findPeakElement([73, 57, 79, 26, 50]) == 2
assert solution.findPeakElement([93, 57, 6, 73]) == 0
assert solution.findPeakElement([66, 44, 18, 68, 24, 92, 56]) == 0
assert solution.findPeakElement([43, 38, 53, 60, 26, 74, 3, 19, 84]) == 8
assert solution.findPeakElement([89, 84, 46, 55, 75, 18, 95, 31]) == 6
assert solution.findPeakElement([57, 6, 81, 35, 97, 62]) == 2
assert solution.findPeakElement([25, 50, 88]) == 2
assert solution.findPeakElement([32, 78, 55, 42, 59, 40, 65, 67, 46, 10]) == 1
assert solution.findPeakElement([93, 47, 72, 27]) == 2
assert solution.findPeakElement([90, 38, 47, 53, 71]) == 4
assert solution.findPeakElement([62, 17, 75, 81, 31, 60, 55, 4]) == 3
assert solution.findPeakElement([51, 100]) == 1
assert solution.findPeakElement([47, 73, 54]) == 1
assert solution.findPeakElement([20, 12, 57, 51, 89, 76, 52, 63, 25]) == 2
assert solution.findPeakElement([1, 67]) == 1
assert solution.findPeakElement([44, 79]) == 1
assert solution.findPeakElement([64, 69, 12, 26, 4]) == 3
assert solution.findPeakElement([74, 53, 84, 28, 43, 30, 6, 69, 2]) == 2
assert solution.findPeakElement([4, 90, 75, 67, 100]) == 1
assert solution.findPeakElement([3, 94, 76, 1]) == 1
assert solution.findPeakElement([3, 100, 2, 52, 85, 89]) == 5
assert solution.findPeakElement([78, 50, 88]) == 2
assert solution.findPeakElement([28, 88, 94]) == 2
assert solution.findPeakElement([37, 5, 55, 80, 48, 19, 24, 65, 33, 41]) == 3
assert solution.findPeakElement([60, 83, 53]) == 1
assert solution.findPeakElement([80, 57, 54, 56, 12, 9, 66]) == 0
assert solution.findPeakElement([19, 21, 25, 55, 61, 46, 56, 51, 57, 2]) == 4
assert solution.findPeakElement([5, 54, 74, 22, 28, 42, 58]) == 6
assert solution.findPeakElement([27, 7, 90, 56, 5, 82, 63, 41, 86]) == 5
assert solution.findPeakElement([84, 80, 11, 79, 60, 41, 23, 98, 85, 96]) == 3
assert solution.findPeakElement([6, 26, 20]) == 1
assert solution.findPeakElement([42, 92, 27, 3, 11, 31, 9, 83]) == 5
assert solution.findPeakElement([19, 74, 27, 53, 92]) == 4
assert solution.findPeakElement([15, 98, 72, 54, 7]) == 1
assert solution.findPeakElement([64, 38, 49]) == 2
assert solution.findPeakElement([40, 13, 46, 80, 75, 67, 99, 76]) == 3
assert solution.findPeakElement([13, 97, 47, 76, 100, 56]) == 4
assert solution.findPeakElement([76, 86, 16]) == 1
assert solution.findPeakElement([95, 11, 99, 22, 10, 87]) == 2
assert solution.findPeakElement([97, 69, 70, 14, 45, 39, 81]) == 6
assert solution.findPeakElement([91, 28, 31, 68, 49, 33, 57]) == 3
assert solution.findPeakElement([67, 29]) == 0
assert solution.findPeakElement([20, 37, 59, 1]) == 2
assert solution.findPeakElement([29, 62, 18, 95, 9, 32]) == 5