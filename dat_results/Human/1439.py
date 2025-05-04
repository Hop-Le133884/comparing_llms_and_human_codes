
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
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        pre = [0]
        for cur in mat:
            pre = sorted(a + b for a in pre for b in cur[:k])[:k]
        return pre[-1]

solution=Solution()
assert solution.kthSmallest([[18, 24, 33, 62, 80], [1, 18, 38, 83, 84], [5, 17, 20, 21, 45]], 48) == 96
assert solution.kthSmallest([[12, 50, 74, 77, 85, 96], [17, 43, 51, 58, 74, 92]], 21) == 132
assert solution.kthSmallest([[31, 39], [24, 37], [68, 99]], 4) == 144
assert solution.kthSmallest([[8, 67, 76, 79, 82, 86], [21, 40, 44, 50, 62, 95], [14, 46, 53, 67, 76, 90], [9, 11, 36, 72, 81, 98]], 39) == 120
assert solution.kthSmallest([[17, 63, 66, 86, 99], [25, 42, 62, 75, 86], [44, 62, 80, 96, 98]], 21) == 155
assert solution.kthSmallest([[10, 19, 29, 74, 77, 100], [3, 5, 11, 19, 29, 63], [33, 46, 50, 54, 65, 84], [12, 20, 49, 82, 92, 98]], 113) == 108
assert solution.kthSmallest([[9, 40, 83, 95], [18, 38, 70, 81], [19, 27, 79, 96], [10, 48, 72, 76], [4, 43, 81, 100]], 111) == 184
assert solution.kthSmallest([[48, 88], [53, 69], [33, 48]], 5) == 174
assert solution.kthSmallest([[6, 11, 54, 80, 82, 86], [3, 18, 28, 58, 85, 92], [6, 8, 11, 22, 43, 59], [42, 43, 50, 82, 83, 92]], 142) == 120
assert solution.kthSmallest([[1, 56, 65, 79, 92], [7, 23, 54, 60, 63], [9, 28, 35, 69, 70], [5, 15, 42, 67, 82]], 162) == 149
assert solution.kthSmallest([[18, 62, 67, 75, 80], [8, 15, 32, 54, 68], [8, 42, 43, 51, 94], [18, 39, 58, 81, 93]], 105) == 152
assert solution.kthSmallest([[4, 50], [16, 71], [20, 82]], 1) == 40
assert solution.kthSmallest([[15, 40, 80, 83], [7, 26, 56, 94], [49, 68, 69, 87], [2, 3, 22, 27]], 94) == 162
assert solution.kthSmallest([[70, 78], [11, 72], [42, 61], [63, 99], [36, 75], [43, 93]], 22) == 351
assert solution.kthSmallest([[21, 48, 53, 62, 77, 90], [22, 26, 55, 57, 73, 91], [40, 44, 66, 85, 87, 100], [54, 60, 83, 92, 94, 100]], 79) == 196
assert solution.kthSmallest([[17, 22, 35, 40, 64, 80], [41, 45, 47, 65, 71, 96], [11, 44, 52, 61, 66, 98], [8, 14, 17, 23, 39, 52], [28, 33, 43, 72, 77, 93]], 105) == 140
assert solution.kthSmallest([[24, 50, 53, 81, 84, 93], [21, 23, 28, 37, 83, 88]], 22) == 116
assert solution.kthSmallest([[42, 44, 48, 85], [12, 13, 24, 86], [34, 53, 87, 96]], 6) == 95
assert solution.kthSmallest([[1, 10, 78, 83, 90], [19, 55, 73, 75, 92], [36, 40, 53, 76, 90], [20, 32, 34, 61, 84]], 6) == 90
assert solution.kthSmallest([[16, 53, 78], [4, 18, 30]], 7) == 83
assert solution.kthSmallest([[23, 50, 86], [39, 57, 76], [8, 73, 88]], 2) == 88
assert solution.kthSmallest([[15, 68, 92, 97], [2, 7, 52, 65], [20, 62, 79, 99], [22, 49, 59, 70]], 67) == 178
assert solution.kthSmallest([[44, 50, 66], [16, 56, 70], [9, 37, 98], [41, 63, 65], [1, 23, 72], [2, 80, 83]], 166) == 241
assert solution.kthSmallest([[21, 71, 84, 88], [32, 47, 53, 92], [4, 24, 39, 74], [3, 16, 30, 71]], 17) == 108
assert solution.kthSmallest([[1, 2, 14, 34, 42, 91], [17, 37, 56, 57, 61, 77], [38, 54, 68, 87, 92, 93], [8, 29, 39, 59, 67, 78], [14, 38, 61, 84, 89, 95], [9, 29, 41, 57, 86, 96]], 194) == 155
assert solution.kthSmallest([[26, 33, 49, 61, 68], [11, 31, 50, 51, 56], [10, 18, 24, 50, 87]], 39) == 103
assert solution.kthSmallest([[48, 79], [65, 80], [12, 64], [47, 71]], 10) == 242
assert solution.kthSmallest([[36, 84, 89, 92, 96], [4, 36, 61, 72, 98], [22, 39, 66, 85, 93], [16, 42, 83, 88, 98]], 36) == 164
assert solution.kthSmallest([[34, 74], [2, 30]], 1) == 36
assert solution.kthSmallest([[35, 63, 84], [28, 64, 89], [5, 38, 95]], 27) == 268
assert solution.kthSmallest([[8, 9, 28, 43], [10, 29, 31, 36], [2, 3, 54, 81]], 18) == 48
assert solution.kthSmallest([[11, 17, 24, 74, 77, 78], [1, 17, 28, 40, 81, 100], [12, 30, 49, 53, 55, 78], [3, 27, 30, 48, 67, 75], [9, 16, 24, 55, 69, 99], [37, 43, 62, 72, 74, 96]], 117) == 118
assert solution.kthSmallest([[3, 4, 22, 41, 44, 99], [1, 35, 44, 54, 75, 90], [3, 18, 25, 28, 81, 89], [3, 11, 18, 22, 25, 61]], 15) == 33
assert solution.kthSmallest([[8, 26, 29, 35, 57], [27, 47, 56, 57, 73], [27, 44, 61, 94, 99], [1, 36, 49, 70, 94], [2, 6, 30, 42, 88]], 39) == 112
assert solution.kthSmallest([[8, 56], [26, 67], [49, 81], [96, 97], [4, 88]], 3) == 215
assert solution.kthSmallest([[86, 94], [10, 24], [1, 18]], 8) == 136
assert solution.kthSmallest([[20, 37, 54], [52, 53, 90], [67, 77, 91], [61, 62, 86]], 64) == 272
assert solution.kthSmallest([[21, 24, 50, 70, 76, 87], [23, 25, 26, 62, 63, 83], [7, 13, 34, 35, 54, 88], [18, 21, 29, 32, 35, 76], [9, 14, 26, 45, 75, 98]], 196) == 114
assert solution.kthSmallest([[18, 40, 50, 61], [5, 64, 77, 79]], 2) == 45
assert solution.kthSmallest([[12, 71, 93], [20, 59, 100], [38, 46, 70], [10, 29, 48], [22, 51, 76]], 104) == 238
assert solution.kthSmallest([[39, 56, 67, 72], [38, 58, 62, 69], [11, 49, 68, 93], [44, 69, 75, 78]], 97) == 225
assert solution.kthSmallest([[29, 31, 36, 84, 92], [9, 21, 39, 41, 93], [50, 80, 82, 87, 93], [35, 38, 41, 78, 95]], 2) == 125
assert solution.kthSmallest([[64, 78, 99], [23, 41, 69], [8, 14, 37], [4, 14, 21]], 27) == 144
assert solution.kthSmallest([[16, 56, 63, 91], [39, 72, 80, 86], [12, 18, 25, 51], [27, 44, 68, 78], [31, 36, 39, 57], [16, 27, 80, 92]], 183) == 208
assert solution.kthSmallest([[32, 60, 63], [57, 85, 89], [14, 20, 27], [3, 15, 18], [9, 16, 43]], 72) == 168
assert solution.kthSmallest([[36, 55, 60, 64, 89], [9, 13, 43, 45, 78], [5, 46, 48, 75, 97], [10, 16, 50, 69, 76]], 183) == 166
assert solution.kthSmallest([[20, 45, 53, 58, 74, 93], [5, 18, 23, 39, 43, 70]], 1) == 25
assert solution.kthSmallest([[55, 99], [73, 78]], 4) == 177
assert solution.kthSmallest([[20, 53, 60, 62, 89], [8, 29, 46, 51, 87]], 22) == 140
assert solution.kthSmallest([[80, 90], [6, 43], [28, 68]], 6) == 164
assert solution.kthSmallest([[5, 9, 12, 17, 52], [49, 58, 81, 83, 96], [7, 23, 30, 57, 78], [12, 17, 50, 56, 92], [9, 13, 30, 58, 83]], 22) == 99
assert solution.kthSmallest([[17, 56, 75, 96], [1, 20, 21, 60], [32, 48, 49, 62], [19, 29, 59, 87], [13, 58, 61, 92], [43, 47, 58, 96]], 96) == 186
assert solution.kthSmallest([[3, 28, 55, 71, 99], [27, 42, 50, 54, 83], [3, 12, 17, 44, 96]], 66) == 138
assert solution.kthSmallest([[56, 58, 67, 92, 93, 95], [12, 21, 25, 39, 45, 98]], 3) == 77
assert solution.kthSmallest([[22, 32, 38, 80], [18, 41, 52, 65], [13, 47, 48, 76], [3, 50, 63, 70]], 102) == 169
assert solution.kthSmallest([[1, 12, 21, 28, 30, 36], [7, 26, 60, 78, 79, 81], [27, 34, 39, 46, 55, 92], [20, 30, 40, 52, 56, 59], [13, 17, 36, 39, 51, 89]], 68) == 103
assert solution.kthSmallest([[35, 91], [44, 48]], 2) == 83
assert solution.kthSmallest([[15, 49, 83, 100], [36, 38, 67, 85], [34, 78, 88, 98]], 23) == 173
assert solution.kthSmallest([[29, 45, 100], [19, 39, 98], [8, 81, 94], [50, 76, 91], [11, 23, 98], [18, 68, 81]], 96) == 254
assert solution.kthSmallest([[3, 51], [5, 57], [31, 100]], 4) == 108
assert solution.kthSmallest([[2, 16, 20, 39, 53, 91], [10, 19, 44, 79, 88, 91], [2, 6, 41, 48, 91, 97], [1, 6, 9, 30, 37, 75], [13, 15, 26, 53, 84, 92]], 94) == 64
assert solution.kthSmallest([[12, 38], [28, 83], [61, 87], [22, 62]], 9) == 204
assert solution.kthSmallest([[1, 4, 18, 51, 100], [21, 28, 32, 59, 99]], 1) == 22
assert solution.kthSmallest([[2, 5, 13, 43, 94], [6, 17, 67, 73, 75]], 22) == 118
assert solution.kthSmallest([[3, 50], [30, 67], [4, 24], [11, 41], [39, 88]], 7) == 137
assert solution.kthSmallest([[71, 78, 88], [1, 24, 55]], 7) == 126
assert solution.kthSmallest([[21, 52], [7, 37], [25, 39], [12, 24]], 7) == 107
assert solution.kthSmallest([[8, 12, 35, 54, 76], [4, 25, 29, 61, 62], [8, 42, 46, 59, 62], [13, 25, 54, 87, 94], [9, 32, 49, 53, 57]], 200) == 128
assert solution.kthSmallest([[18, 27, 38, 62], [13, 42, 64, 77], [34, 42, 52, 81], [30, 45, 48, 93]], 194) == 221
assert solution.kthSmallest([[19, 51, 95], [12, 17, 86], [60, 75, 86]], 1) == 91
assert solution.kthSmallest([[13, 18, 24, 51, 79, 100], [31, 37, 60, 67, 93, 96]], 13) == 88
assert solution.kthSmallest([[32, 84], [68, 70], [4, 5], [75, 92], [46, 85]], 28) == 319
assert solution.kthSmallest([[33, 44, 85], [41, 68, 98], [53, 70, 81], [35, 49, 97], [21, 29, 70]], 24) == 227
assert solution.kthSmallest([[3, 8, 43, 45], [16, 30, 85, 95]], 5) == 59
assert solution.kthSmallest([[60, 89], [45, 48], [1, 67], [21, 39]], 1) == 127
assert solution.kthSmallest([[5, 100], [28, 40], [56, 58], [67, 77], [47, 96], [18, 71]], 24) == 298
assert solution.kthSmallest([[16, 35, 62, 75], [15, 22, 36, 86], [28, 35, 43, 52], [2, 40, 45, 84], [13, 31, 43, 95]], 96) == 141
assert solution.kthSmallest([[25, 29, 31, 45, 51, 95], [33, 40, 43, 76, 80, 97], [11, 41, 60, 75, 81, 90], [11, 39, 40, 43, 47, 76]], 138) == 151
assert solution.kthSmallest([[15, 66, 72, 82], [6, 62, 71, 93]], 11) == 143
assert solution.kthSmallest([[12, 16, 27, 57, 75, 98], [15, 16, 19, 31, 38, 100], [22, 29, 47, 54, 83, 93], [10, 13, 26, 44, 68, 88]], 79) == 92
assert solution.kthSmallest([[65, 71], [1, 42], [8, 64], [2, 79]], 16) == 256
assert solution.kthSmallest([[5, 40, 42, 53, 62, 77], [25, 41, 51, 71, 73, 99], [3, 20, 35, 55, 79, 89], [20, 35, 51, 54, 79, 95], [36, 46, 56, 80, 82, 87]], 133) == 158
assert solution.kthSmallest([[59, 98], [65, 91], [12, 28], [21, 70], [87, 90]], 24) == 335
assert solution.kthSmallest([[42, 55], [53, 79]], 4) == 134
assert solution.kthSmallest([[19, 25, 38, 41, 43, 62], [24, 25, 56, 68, 72, 92], [6, 8, 15, 38, 51, 82], [12, 23, 55, 64, 72, 89]], 190) == 128
assert solution.kthSmallest([[14, 89, 97], [28, 90, 96], [3, 32, 38], [12, 42, 48], [11, 73, 92]], 181) == 302
assert solution.kthSmallest([[14, 16, 30, 31, 65, 97], [6, 15, 46, 53, 57, 88], [24, 44, 51, 55, 58, 85]], 103) == 131
assert solution.kthSmallest([[1, 12, 21, 68], [39, 54, 57, 89], [43, 48, 55, 67], [32, 47, 70, 93], [57, 73, 81, 95]], 6) == 187
assert solution.kthSmallest([[15, 48, 52, 59, 80], [1, 2, 3, 27, 64], [19, 25, 26, 66, 80], [19, 21, 49, 87, 92]], 2) == 55
assert solution.kthSmallest([[17, 89], [28, 90]], 4) == 179
assert solution.kthSmallest([[10, 23, 62, 64, 90, 99], [33, 40, 78, 91, 96, 99], [29, 46, 47, 57, 67, 86], [16, 24, 27, 37, 68, 85], [4, 14, 34, 40, 56, 68], [11, 21, 38, 45, 51, 82]], 190) == 151
assert solution.kthSmallest([[1, 7, 54, 74, 93], [18, 19, 48, 49, 88], [54, 63, 88, 96, 99], [35, 39, 46, 66, 91], [17, 60, 68, 86, 98], [26, 46, 71, 74, 92]], 144) == 206
assert solution.kthSmallest([[20, 85], [18, 63], [31, 36]], 6) == 139
assert solution.kthSmallest([[4, 9, 30], [29, 53, 80], [14, 76, 78], [52, 54, 81]], 34) == 184
assert solution.kthSmallest([[46, 75, 84], [40, 97, 100], [39, 49, 54], [7, 47, 68], [1, 38, 58]], 14) == 186
assert solution.kthSmallest([[62, 79, 94, 95], [22, 23, 87, 96], [22, 54, 77, 78], [29, 37, 73, 89], [20, 25, 41, 86]], 10) == 173
assert solution.kthSmallest([[33, 51, 69, 72, 89], [6, 14, 18, 68, 80]], 10) == 86
assert solution.kthSmallest([[22, 34, 54, 81, 88], [22, 27, 50, 57, 60]], 6) == 76
assert solution.kthSmallest([[3, 40], [40, 92], [62, 73]], 2) == 116
assert solution.kthSmallest([[6, 47], [49, 81], [2, 26], [22, 61], [6, 84]], 16) == 189