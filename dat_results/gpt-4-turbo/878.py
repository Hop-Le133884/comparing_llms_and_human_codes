
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


# hard_nthMagicalNumber.py

class Solution:
    def nthMagicalNumber(self, n, a, b):
        MOD = 10**9 + 7

        # Helper function to calculate Least Common Multiple (LCM) of a and b
        def lcm(x, y):
            from math import gcd
            return x * y // gcd(x, y)

        # Binary search to find the nth magical number
        left, right = min(a, b), n * min(a, b)
        lcm_ab = lcm(a, b)

        while left < right:
            mid = (left + right) // 2
            if mid // a + mid // b - mid // lcm_ab >= n:
                right = mid
            else:
                left = mid + 1

        return left % MOD


solution=Solution()
assert solution.nthMagicalNumber(29, 235, 850) == 5405
assert solution.nthMagicalNumber(39, 979, 414) == 11592
assert solution.nthMagicalNumber(59, 702, 215) == 9828
assert solution.nthMagicalNumber(54, 36, 819) == 1872
assert solution.nthMagicalNumber(62, 996, 54) == 3186
assert solution.nthMagicalNumber(29, 751, 99) == 2574
assert solution.nthMagicalNumber(76, 231, 775) == 13629
assert solution.nthMagicalNumber(31, 490, 347) == 6370
assert solution.nthMagicalNumber(100, 152, 700) == 12600
assert solution.nthMagicalNumber(36, 682, 807) == 13640
assert solution.nthMagicalNumber(69, 119, 575) == 6900
assert solution.nthMagicalNumber(91, 289, 55) == 4235
assert solution.nthMagicalNumber(21, 63, 334) == 1134
assert solution.nthMagicalNumber(67, 136, 186) == 5304
assert solution.nthMagicalNumber(18, 226, 264) == 2260
assert solution.nthMagicalNumber(60, 883, 434) == 17660
assert solution.nthMagicalNumber(99, 461, 265) == 16695
assert solution.nthMagicalNumber(21, 48, 969) == 969
assert solution.nthMagicalNumber(48, 264, 495) == 8712
assert solution.nthMagicalNumber(82, 715, 763) == 30520
assert solution.nthMagicalNumber(28, 238, 570) == 4760
assert solution.nthMagicalNumber(25, 275, 99) == 1881
assert solution.nthMagicalNumber(41, 644, 103) == 3708
assert solution.nthMagicalNumber(63, 38, 396) == 2204
assert solution.nthMagicalNumber(84, 631, 966) == 32181
assert solution.nthMagicalNumber(72, 448, 109) == 6322
assert solution.nthMagicalNumber(53, 529, 9) == 477
assert solution.nthMagicalNumber(44, 788, 583) == 14972
assert solution.nthMagicalNumber(72, 201, 585) == 10854
assert solution.nthMagicalNumber(87, 110, 802) == 8470
assert solution.nthMagicalNumber(79, 687, 120) == 8160
assert solution.nthMagicalNumber(44, 730, 839) == 17520
assert solution.nthMagicalNumber(42, 306, 493) == 7956
assert solution.nthMagicalNumber(90, 722, 861) == 35378
assert solution.nthMagicalNumber(40, 941, 263) == 8416
assert solution.nthMagicalNumber(68, 657, 566) == 20942
assert solution.nthMagicalNumber(27, 56, 436) == 1344
assert solution.nthMagicalNumber(33, 359, 21) == 672
assert solution.nthMagicalNumber(62, 310, 754) == 13640
assert solution.nthMagicalNumber(55, 880, 517) == 18095
assert solution.nthMagicalNumber(31, 629, 24) == 720
assert solution.nthMagicalNumber(9, 197, 942) == 1576
assert solution.nthMagicalNumber(82, 717, 581) == 26529
assert solution.nthMagicalNumber(19, 407, 43) == 774
assert solution.nthMagicalNumber(96, 355, 349) == 17040
assert solution.nthMagicalNumber(56, 102, 350) == 4488
assert solution.nthMagicalNumber(47, 252, 139) == 4284
assert solution.nthMagicalNumber(47, 571, 43) == 1892
assert solution.nthMagicalNumber(26, 926, 447) == 8046
assert solution.nthMagicalNumber(53, 554, 612) == 15512
assert solution.nthMagicalNumber(56, 438, 461) == 12702
assert solution.nthMagicalNumber(10, 742, 719) == 3710
assert solution.nthMagicalNumber(59, 841, 455) == 17661
assert solution.nthMagicalNumber(80, 201, 81) == 4623
assert solution.nthMagicalNumber(99, 131, 550) == 10480
assert solution.nthMagicalNumber(16, 192, 826) == 2496
assert solution.nthMagicalNumber(93, 971, 28) == 2548
assert solution.nthMagicalNumber(81, 899, 653) == 30691
assert solution.nthMagicalNumber(33, 413, 77) == 2156
assert solution.nthMagicalNumber(24, 108, 971) == 2376
assert solution.nthMagicalNumber(22, 61, 612) == 1224
assert solution.nthMagicalNumber(11, 465, 192) == 1536
assert solution.nthMagicalNumber(33, 933, 866) == 14928
assert solution.nthMagicalNumber(28, 615, 885) == 10455
assert solution.nthMagicalNumber(13, 49, 577) == 588
assert solution.nthMagicalNumber(71, 726, 190) == 10830
assert solution.nthMagicalNumber(46, 49, 729) == 2156
assert solution.nthMagicalNumber(78, 821, 432) == 22167
assert solution.nthMagicalNumber(69, 942, 616) == 25872
assert solution.nthMagicalNumber(53, 543, 293) == 10255
assert solution.nthMagicalNumber(96, 660, 238) == 16898
assert solution.nthMagicalNumber(90, 908, 16) == 1424
assert solution.nthMagicalNumber(74, 955, 324) == 18144
assert solution.nthMagicalNumber(8, 196, 448) == 1176
assert solution.nthMagicalNumber(31, 381, 713) == 7843
assert solution.nthMagicalNumber(24, 872, 249) == 4731
assert solution.nthMagicalNumber(99, 267, 335) == 14740
assert solution.nthMagicalNumber(2, 58, 577) == 116
assert solution.nthMagicalNumber(53, 343, 463) == 10633
assert solution.nthMagicalNumber(7, 918, 264) == 1584
assert solution.nthMagicalNumber(18, 648, 611) == 5832
assert solution.nthMagicalNumber(18, 849, 200) == 3000
assert solution.nthMagicalNumber(88, 886, 933) == 40119
assert solution.nthMagicalNumber(14, 631, 27) == 378
assert solution.nthMagicalNumber(20, 838, 496) == 6448
assert solution.nthMagicalNumber(43, 835, 644) == 15865
assert solution.nthMagicalNumber(92, 464, 868) == 27840
assert solution.nthMagicalNumber(66, 491, 428) == 15221
assert solution.nthMagicalNumber(31, 98, 521) == 2605
assert solution.nthMagicalNumber(10, 271, 299) == 1495
assert solution.nthMagicalNumber(86, 499, 233) == 13747
assert solution.nthMagicalNumber(20, 355, 692) == 4844
assert solution.nthMagicalNumber(92, 360, 637) == 21240
assert solution.nthMagicalNumber(15, 524, 21) == 315
assert solution.nthMagicalNumber(38, 209, 227) == 4180
assert solution.nthMagicalNumber(72, 117, 43) == 2279
assert solution.nthMagicalNumber(43, 554, 207) == 6624
assert solution.nthMagicalNumber(98, 199, 377) == 12818
assert solution.nthMagicalNumber(40, 896, 668) == 15364
assert solution.nthMagicalNumber(24, 936, 372) == 6552