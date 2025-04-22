
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
    def findNthDigit(self, n):
        length = 1
        count = 9
        start = 1
        
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        start += (n - 1) // length
        s = str(start)
        return int(s[(n - 1) % length])


solution=Solution()
assert solution.findNthDigit(46) == 2
assert solution.findNthDigit(26) == 1
assert solution.findNthDigit(79) == 4
assert solution.findNthDigit(36) == 2
assert solution.findNthDigit(60) == 3
assert solution.findNthDigit(58) == 3
assert solution.findNthDigit(12) == 1
assert solution.findNthDigit(60) == 3
assert solution.findNthDigit(93) == 1
assert solution.findNthDigit(98) == 5
assert solution.findNthDigit(5) == 5
assert solution.findNthDigit(23) == 6
assert solution.findNthDigit(79) == 4
assert solution.findNthDigit(2) == 2
assert solution.findNthDigit(8) == 8
assert solution.findNthDigit(41) == 5
assert solution.findNthDigit(36) == 2
assert solution.findNthDigit(56) == 3
assert solution.findNthDigit(81) == 5
assert solution.findNthDigit(18) == 1
assert solution.findNthDigit(52) == 3
assert solution.findNthDigit(69) == 9
assert solution.findNthDigit(75) == 2
assert solution.findNthDigit(86) == 4
assert solution.findNthDigit(87) == 8
assert solution.findNthDigit(16) == 1
assert solution.findNthDigit(43) == 6
assert solution.findNthDigit(23) == 6
assert solution.findNthDigit(72) == 4
assert solution.findNthDigit(58) == 3
assert solution.findNthDigit(43) == 6
assert solution.findNthDigit(34) == 2
assert solution.findNthDigit(19) == 4
assert solution.findNthDigit(56) == 3
assert solution.findNthDigit(64) == 3
assert solution.findNthDigit(81) == 5
assert solution.findNthDigit(19) == 4
assert solution.findNthDigit(6) == 6
assert solution.findNthDigit(98) == 5
assert solution.findNthDigit(40) == 2
assert solution.findNthDigit(13) == 1
assert solution.findNthDigit(81) == 5
assert solution.findNthDigit(90) == 5
assert solution.findNthDigit(88) == 4
assert solution.findNthDigit(54) == 3
assert solution.findNthDigit(60) == 3
assert solution.findNthDigit(30) == 2
assert solution.findNthDigit(7) == 7
assert solution.findNthDigit(46) == 2
assert solution.findNthDigit(5) == 5
assert solution.findNthDigit(26) == 1
assert solution.findNthDigit(99) == 4
assert solution.findNthDigit(30) == 2
assert solution.findNthDigit(10) == 1
assert solution.findNthDigit(77) == 3
assert solution.findNthDigit(83) == 6
assert solution.findNthDigit(99) == 4
assert solution.findNthDigit(54) == 3
assert solution.findNthDigit(65) == 7
assert solution.findNthDigit(54) == 3
assert solution.findNthDigit(21) == 5
assert solution.findNthDigit(6) == 6
assert solution.findNthDigit(35) == 2
assert solution.findNthDigit(58) == 3
assert solution.findNthDigit(12) == 1
assert solution.findNthDigit(58) == 3
assert solution.findNthDigit(96) == 5
assert solution.findNthDigit(71) == 0
assert solution.findNthDigit(43) == 6
assert solution.findNthDigit(31) == 0
assert solution.findNthDigit(95) == 2
assert solution.findNthDigit(65) == 7
assert solution.findNthDigit(93) == 1
assert solution.findNthDigit(40) == 2
assert solution.findNthDigit(64) == 3
assert solution.findNthDigit(86) == 4
assert solution.findNthDigit(19) == 4
assert solution.findNthDigit(38) == 2
assert solution.findNthDigit(57) == 3
assert solution.findNthDigit(74) == 4
assert solution.findNthDigit(59) == 4
assert solution.findNthDigit(66) == 3
assert solution.findNthDigit(86) == 4
assert solution.findNthDigit(55) == 2
assert solution.findNthDigit(47) == 8
assert solution.findNthDigit(43) == 6
assert solution.findNthDigit(97) == 3
assert solution.findNthDigit(71) == 0
assert solution.findNthDigit(48) == 2
assert solution.findNthDigit(27) == 8
assert solution.findNthDigit(55) == 2
assert solution.findNthDigit(86) == 4
assert solution.findNthDigit(21) == 5
assert solution.findNthDigit(19) == 4
assert solution.findNthDigit(8) == 8
assert solution.findNthDigit(61) == 5
assert solution.findNthDigit(93) == 1
assert solution.findNthDigit(87) == 8
assert solution.findNthDigit(89) == 9
assert solution.findNthDigit(51) == 0