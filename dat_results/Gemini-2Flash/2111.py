
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


# hard_kIncreasing.py

class Solution:
    def kIncreasing(self, arr: list[int], k: int) -> int:
        """
        Minimum Operations to Make the Array K-increasing
        """

        def longest_non_decreasing_subsequence(sub_arr):
            tails = []
            for num in sub_arr:
                if not tails or num >= tails[-1]:
                    tails.append(num)
                else:
                    l, r = 0, len(tails) - 1
                    while l < r:
                        mid = l + (r - l) // 2
                        if tails[mid] <= num:
                            l = mid + 1
                        else:
                            r = mid
                    tails[l] = num
            return len(tails)

        n = len(arr)
        ans = 0
        for i in range(k):
            sub_arr = [arr[j] for j in range(i, n, k)]
            ans += len(sub_arr) - longest_non_decreasing_subsequence(sub_arr)
        return ans

solution=Solution()
assert solution.kIncreasing([63, 2, 87, 22, 33, 64, 47, 95], 8) == 0
assert solution.kIncreasing([27, 78, 53, 55, 18, 12, 86], 4) == 2
assert solution.kIncreasing([33, 91, 13, 80, 79, 85, 100, 98, 80], 1) == 5
assert solution.kIncreasing([19], 1) == 0
assert solution.kIncreasing([18, 66, 81, 60, 54], 4) == 0
assert solution.kIncreasing([90, 66, 62, 80, 52, 22, 96], 3) == 3
assert solution.kIncreasing([4, 54, 15, 3, 14, 50, 63, 53, 5], 4) == 2
assert solution.kIncreasing([96, 90, 16, 93, 96, 83, 88, 18], 7) == 1
assert solution.kIncreasing([20], 1) == 0
assert solution.kIncreasing([67, 93, 51, 85, 13, 70, 78, 41, 5], 5) == 3
assert solution.kIncreasing([29, 13, 75, 91], 3) == 0
assert solution.kIncreasing([15, 25, 75, 41, 47], 2) == 1
assert solution.kIncreasing([49, 50, 46, 2, 70, 1, 32, 47], 7) == 1
assert solution.kIncreasing([17, 43, 52, 17, 31, 64, 85, 41], 1) == 3
assert solution.kIncreasing([68, 60, 75, 32, 82, 57, 4, 93, 15], 8) == 1
assert solution.kIncreasing([20, 92, 14, 64, 80, 64, 17, 50, 4, 56], 4) == 4
assert solution.kIncreasing([8, 89, 85, 34, 79, 1, 51, 89, 96], 7) == 0
assert solution.kIncreasing([6, 2], 2) == 0
assert solution.kIncreasing([2, 44], 1) == 0
assert solution.kIncreasing([39, 86, 98, 46, 66, 82, 89], 1) == 2
assert solution.kIncreasing([74, 11, 98], 2) == 0
assert solution.kIncreasing([27, 1, 41, 98, 54, 95], 1) == 2
assert solution.kIncreasing([93, 86, 91, 14, 55], 3) == 2
assert solution.kIncreasing([70, 98, 40, 92, 31, 87, 19, 72, 55, 11], 8) == 2
assert solution.kIncreasing([40, 61, 3, 99], 1) == 1
assert solution.kIncreasing([4, 30, 12], 2) == 0
assert solution.kIncreasing([7, 49, 91], 3) == 0
assert solution.kIncreasing([27, 8, 26, 31, 54, 28, 47, 40, 45], 8) == 0
assert solution.kIncreasing([49, 35, 84, 9, 11, 19, 59, 16, 91, 54], 10) == 0
assert solution.kIncreasing([32, 6], 2) == 0
assert solution.kIncreasing([62, 11, 40, 27, 42, 38, 93], 2) == 1
assert solution.kIncreasing([61, 63, 41, 9, 34, 56, 9, 48], 5) == 2
assert solution.kIncreasing([40, 51], 2) == 0
assert solution.kIncreasing([42, 63, 58, 83, 14, 79, 70], 2) == 2
assert solution.kIncreasing([27, 98, 10, 58, 49, 23], 5) == 1
assert solution.kIncreasing([58, 15, 77, 1, 84, 42], 4) == 0
assert solution.kIncreasing([7, 92, 14, 30, 5, 22, 64, 69, 69], 8) == 0
assert solution.kIncreasing([47, 19, 88, 36, 96, 27, 96, 41], 5) == 2
assert solution.kIncreasing([22, 36, 86, 66, 55, 28], 6) == 0
assert solution.kIncreasing([92, 14, 90, 78, 100, 65, 50, 60, 42, 94], 5) == 4
assert solution.kIncreasing([97, 62, 9], 3) == 0
assert solution.kIncreasing([40, 78], 1) == 0
assert solution.kIncreasing([100, 73, 40, 70, 80, 29], 6) == 0
assert solution.kIncreasing([95, 58, 51, 84, 43, 49, 3, 7, 38, 4], 7) == 3
assert solution.kIncreasing([74, 92, 68, 4], 2) == 2
assert solution.kIncreasing([91, 47, 16, 33, 34, 33, 99, 48, 58, 28], 6) == 1
assert solution.kIncreasing([81, 32, 9, 68, 7, 80], 6) == 0
assert solution.kIncreasing([35, 27, 11, 66, 93, 41, 69, 90, 69, 11], 2) == 4
assert solution.kIncreasing([17, 51, 36], 3) == 0
assert solution.kIncreasing([84], 1) == 0
assert solution.kIncreasing([81, 16, 44, 63, 15], 3) == 2
assert solution.kIncreasing([75, 34, 80], 3) == 0
assert solution.kIncreasing([81, 55, 11, 16, 12, 34, 96], 5) == 1
assert solution.kIncreasing([62, 78, 59, 31], 2) == 2
assert solution.kIncreasing([15, 93, 66, 46], 3) == 0
assert solution.kIncreasing([85, 41], 1) == 1
assert solution.kIncreasing([87, 67, 53, 69, 97, 84, 10, 89, 54], 8) == 1
assert solution.kIncreasing([17, 28, 57, 35, 22, 24, 49], 7) == 0
assert solution.kIncreasing([77, 30, 13, 75, 40, 94, 86], 2) == 1
assert solution.kIncreasing([15, 23, 27], 1) == 0
assert solution.kIncreasing([84, 41, 44, 43, 28, 77, 58, 31], 2) == 3
assert solution.kIncreasing([62, 78, 31, 52, 38, 44], 6) == 0
assert solution.kIncreasing([27, 40, 3, 41, 28, 73], 5) == 0
assert solution.kIncreasing([73, 92, 78, 44, 61, 70], 3) == 3
assert solution.kIncreasing([75, 60, 16, 78, 28], 1) == 3
assert solution.kIncreasing([44, 35], 2) == 0
assert solution.kIncreasing([66, 12, 22, 14], 1) == 2
assert solution.kIncreasing([92, 88, 24, 45, 18, 30, 20, 98, 28], 8) == 1
assert solution.kIncreasing([77, 22, 22, 75, 9, 42, 18, 16], 8) == 0
assert solution.kIncreasing([46, 49, 88, 16, 55, 10], 1) == 3
assert solution.kIncreasing([39, 42, 75, 41, 80, 61, 20, 20], 8) == 0
assert solution.kIncreasing([1, 31, 93, 24], 1) == 1
assert solution.kIncreasing([70, 88, 77, 78, 1, 99, 68, 50, 5, 92], 5) == 3
assert solution.kIncreasing([21, 71, 2, 75, 17, 58, 13, 33], 6) == 2
assert solution.kIncreasing([67, 28, 69, 90, 42], 3) == 0
assert solution.kIncreasing([44], 1) == 0
assert solution.kIncreasing([82, 67, 49, 6, 55, 29, 9], 7) == 0
assert solution.kIncreasing([69, 24, 25, 3, 76, 87, 36], 1) == 3
assert solution.kIncreasing([83, 61, 9, 66], 2) == 1
assert solution.kIncreasing([6], 1) == 0
assert solution.kIncreasing([43, 82, 58, 33, 15, 38, 2, 29, 7], 6) == 3
assert solution.kIncreasing([96, 60, 2, 11, 48, 25, 95, 39, 3], 6) == 2
assert solution.kIncreasing([41, 62, 9], 1) == 1
assert solution.kIncreasing([1, 59, 59, 81, 38, 9, 75, 54, 81], 6) == 1
assert solution.kIncreasing([81, 74, 44, 75, 66, 94, 44, 20, 53], 7) == 2
assert solution.kIncreasing([61, 82], 2) == 0
assert solution.kIncreasing([45, 7], 2) == 0
assert solution.kIncreasing([47, 3], 2) == 0
assert solution.kIncreasing([7], 1) == 0
assert solution.kIncreasing([34, 77, 84, 63], 2) == 1
assert solution.kIncreasing([30, 18, 67, 51, 50, 88, 69, 56, 75, 97], 2) == 2
assert solution.kIncreasing([38, 70, 86, 72, 22, 37], 1) == 3
assert solution.kIncreasing([35, 80, 6, 30, 96, 80, 27], 6) == 1
assert solution.kIncreasing([52, 35], 2) == 0
assert solution.kIncreasing([69, 63, 85, 35, 57], 3) == 2
assert solution.kIncreasing([26, 24, 33, 58], 4) == 0
assert solution.kIncreasing([27, 65, 43, 6, 2, 8, 58, 71, 54, 39], 4) == 2
assert solution.kIncreasing([81, 10, 55, 30, 1, 73, 23, 25, 45, 6], 10) == 0
assert solution.kIncreasing([100, 56, 69, 83, 85, 31], 3) == 2
assert solution.kIncreasing([77, 42, 1, 37, 52], 3) == 1