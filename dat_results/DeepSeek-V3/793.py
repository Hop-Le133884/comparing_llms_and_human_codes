
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
    def preimageSizeFZF(self, k):
        def zeta(x):
            res = 0
            while x > 0:
                x = x // 5
                res += x
            return res
        
        left, right = 0, 5 * (k + 1)
        while left <= right:
            mid = (left + right) // 2
            zeros = zeta(mid)
            if zeros == k:
                return 5
            elif zeros < k:
                left = mid + 1
            else:
                right = mid - 1
        return 0

solution=Solution()
assert solution.preimageSizeFZF(51) == 5
assert solution.preimageSizeFZF(100) == 5
assert solution.preimageSizeFZF(84) == 5
assert solution.preimageSizeFZF(62) == 5
assert solution.preimageSizeFZF(73) == 0
assert solution.preimageSizeFZF(76) == 5
assert solution.preimageSizeFZF(27) == 5
assert solution.preimageSizeFZF(51) == 5
assert solution.preimageSizeFZF(85) == 0
assert solution.preimageSizeFZF(38) == 5
assert solution.preimageSizeFZF(48) == 0
assert solution.preimageSizeFZF(35) == 5
assert solution.preimageSizeFZF(20) == 5
assert solution.preimageSizeFZF(94) == 5
assert solution.preimageSizeFZF(62) == 5
assert solution.preimageSizeFZF(74) == 5
assert solution.preimageSizeFZF(70) == 5
assert solution.preimageSizeFZF(33) == 5
assert solution.preimageSizeFZF(21) == 5
assert solution.preimageSizeFZF(35) == 5
assert solution.preimageSizeFZF(95) == 5
assert solution.preimageSizeFZF(38) == 5
assert solution.preimageSizeFZF(14) == 5
assert solution.preimageSizeFZF(26) == 5
assert solution.preimageSizeFZF(8) == 5
assert solution.preimageSizeFZF(21) == 5
assert solution.preimageSizeFZF(8) == 5
assert solution.preimageSizeFZF(4) == 5
assert solution.preimageSizeFZF(92) == 0
assert solution.preimageSizeFZF(20) == 5
assert solution.preimageSizeFZF(51) == 5
assert solution.preimageSizeFZF(90) == 5
assert solution.preimageSizeFZF(83) == 5
assert solution.preimageSizeFZF(59) == 5
assert solution.preimageSizeFZF(37) == 5
assert solution.preimageSizeFZF(44) == 5
assert solution.preimageSizeFZF(58) == 5
assert solution.preimageSizeFZF(12) == 5
assert solution.preimageSizeFZF(23) == 0
assert solution.preimageSizeFZF(77) == 5
assert solution.preimageSizeFZF(67) == 0
assert solution.preimageSizeFZF(99) == 5
assert solution.preimageSizeFZF(85) == 0
assert solution.preimageSizeFZF(29) == 0
assert solution.preimageSizeFZF(96) == 5
assert solution.preimageSizeFZF(72) == 5
assert solution.preimageSizeFZF(60) == 0
assert solution.preimageSizeFZF(66) == 5
assert solution.preimageSizeFZF(28) == 5
assert solution.preimageSizeFZF(12) == 5
assert solution.preimageSizeFZF(91) == 0
assert solution.preimageSizeFZF(85) == 0
assert solution.preimageSizeFZF(1) == 5
assert solution.preimageSizeFZF(7) == 5
assert solution.preimageSizeFZF(19) == 5
assert solution.preimageSizeFZF(82) == 5
assert solution.preimageSizeFZF(44) == 5
assert solution.preimageSizeFZF(65) == 5
assert solution.preimageSizeFZF(80) == 5
assert solution.preimageSizeFZF(60) == 0
assert solution.preimageSizeFZF(89) == 5
assert solution.preimageSizeFZF(29) == 0
assert solution.preimageSizeFZF(68) == 5
assert solution.preimageSizeFZF(69) == 5
assert solution.preimageSizeFZF(91) == 0
assert solution.preimageSizeFZF(14) == 5
assert solution.preimageSizeFZF(90) == 5
assert solution.preimageSizeFZF(90) == 5
assert solution.preimageSizeFZF(60) == 0
assert solution.preimageSizeFZF(24) == 5
assert solution.preimageSizeFZF(24) == 5
assert solution.preimageSizeFZF(86) == 5
assert solution.preimageSizeFZF(68) == 5
assert solution.preimageSizeFZF(82) == 5
assert solution.preimageSizeFZF(64) == 5
assert solution.preimageSizeFZF(30) == 0
assert solution.preimageSizeFZF(6) == 5
assert solution.preimageSizeFZF(30) == 0
assert solution.preimageSizeFZF(99) == 5
assert solution.preimageSizeFZF(47) == 5
assert solution.preimageSizeFZF(61) == 0
assert solution.preimageSizeFZF(58) == 5
assert solution.preimageSizeFZF(91) == 0
assert solution.preimageSizeFZF(79) == 0
assert solution.preimageSizeFZF(98) == 0
assert solution.preimageSizeFZF(28) == 5
assert solution.preimageSizeFZF(99) == 5
assert solution.preimageSizeFZF(7) == 5
assert solution.preimageSizeFZF(30) == 0
assert solution.preimageSizeFZF(66) == 5
assert solution.preimageSizeFZF(62) == 5
assert solution.preimageSizeFZF(87) == 5
assert solution.preimageSizeFZF(98) == 0
assert solution.preimageSizeFZF(60) == 0
assert solution.preimageSizeFZF(46) == 5
assert solution.preimageSizeFZF(93) == 5
assert solution.preimageSizeFZF(78) == 5
assert solution.preimageSizeFZF(58) == 5
assert solution.preimageSizeFZF(45) == 5
assert solution.preimageSizeFZF(98) == 0