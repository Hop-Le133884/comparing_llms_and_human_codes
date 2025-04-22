
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


# hard_findKthNumber.py

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        Kth Smallest Number in Multiplication Table
        """
        left, right = 1, m * n

        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for i in range(1, m + 1):
                count += min(mid // i, n)

            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

solution=Solution()
assert solution.findKthNumber(802, 488, 222929) == 90774
assert solution.findKthNumber(353, 193, 15020) == 3978
assert solution.findKthNumber(427, 932, 63865) == 15105
assert solution.findKthNumber(437, 333, 108367) == 55094
assert solution.findKthNumber(608, 993, 89762) == 20704
assert solution.findKthNumber(418, 394, 93913) == 38346
assert solution.findKthNumber(324, 308, 98762) == 86100
assert solution.findKthNumber(44, 552, 547) == 130
assert solution.findKthNumber(291, 434, 105147) == 60916
assert solution.findKthNumber(701, 539, 53259) == 12138
assert solution.findKthNumber(864, 237, 24300) == 5346
assert solution.findKthNumber(701, 830, 453592) == 241713
assert solution.findKthNumber(108, 749, 41092) == 15696
assert solution.findKthNumber(371, 745, 13937) == 2550
assert solution.findKthNumber(280, 113, 7937) == 2220
assert solution.findKthNumber(447, 297, 82535) == 35868
assert solution.findKthNumber(290, 966, 278381) == 249935
assert solution.findKthNumber(30, 750, 17261) == 9270
assert solution.findKthNumber(728, 605, 395577) == 257754
assert solution.findKthNumber(716, 876, 148448) == 39674
assert solution.findKthNumber(965, 213, 91109) == 32040
assert solution.findKthNumber(849, 540, 406506) == 258842
assert solution.findKthNumber(718, 272, 4782) == 810
assert solution.findKthNumber(662, 876, 119372) == 30420
assert solution.findKthNumber(288, 7, 164) == 64
assert solution.findKthNumber(680, 560, 311447) == 175932
assert solution.findKthNumber(820, 410, 299113) == 191678
assert solution.findKthNumber(825, 910, 438041) == 181152
assert solution.findKthNumber(316, 3, 224) == 123
assert solution.findKthNumber(10, 499, 2033) == 798
assert solution.findKthNumber(20, 729, 2153) == 600
assert solution.findKthNumber(799, 340, 80910) == 23667
assert solution.findKthNumber(543, 525, 15647) == 2896
assert solution.findKthNumber(738, 703, 384335) == 193960
assert solution.findKthNumber(639, 178, 45845) == 15400
assert solution.findKthNumber(198, 874, 58331) == 18034
assert solution.findKthNumber(186, 795, 128731) == 79695
assert solution.findKthNumber(354, 127, 42479) == 31080
assert solution.findKthNumber(349, 92, 9173) == 2698
assert solution.findKthNumber(790, 779, 222077) == 70286
assert solution.findKthNumber(944, 706, 176698) == 49217
assert solution.findKthNumber(647, 481, 128584) == 43488
assert solution.findKthNumber(44, 951, 37006) == 23780
assert solution.findKthNumber(608, 115, 57467) == 32841
assert solution.findKthNumber(645, 248, 2024) == 352
assert solution.findKthNumber(659, 805, 521377) == 435897
assert solution.findKthNumber(251, 386, 89500) == 61870
assert solution.findKthNumber(706, 644, 390482) == 236082
assert solution.findKthNumber(870, 837, 606401) == 350588
assert solution.findKthNumber(265, 326, 3598) == 660
assert solution.findKthNumber(581, 16, 2726) == 904
assert solution.findKthNumber(964, 684, 21454) == 3586
assert solution.findKthNumber(428, 456, 93262) == 34124
assert solution.findKthNumber(742, 715, 94621) == 23042
assert solution.findKthNumber(129, 495, 47119) == 23826
assert solution.findKthNumber(622, 969, 570035) == 416118
assert solution.findKthNumber(904, 831, 570672) == 295481
assert solution.findKthNumber(441, 134, 51167) == 31476
assert solution.findKthNumber(260, 67, 112) == 31
assert solution.findKthNumber(504, 800, 110925) == 31390
assert solution.findKthNumber(549, 625, 257838) == 132098
assert solution.findKthNumber(831, 264, 97207) == 34153
assert solution.findKthNumber(876, 776, 412489) == 175461
assert solution.findKthNumber(847, 434, 311665) == 184926
assert solution.findKthNumber(639, 372, 99068) == 33674
assert solution.findKthNumber(983, 945, 702843) == 362310
assert solution.findKthNumber(470, 569, 26467) == 5530
assert solution.findKthNumber(719, 248, 76620) == 26506
assert solution.findKthNumber(17, 50, 243) == 82
assert solution.findKthNumber(136, 740, 13660) == 3157
assert solution.findKthNumber(662, 128, 8931) == 1950
assert solution.findKthNumber(219, 214, 29018) == 12625
assert solution.findKthNumber(299, 194, 1024) == 190
assert solution.findKthNumber(636, 716, 154733) == 47712
assert solution.findKthNumber(762, 504, 181074) == 65640
assert solution.findKthNumber(465, 637, 57998) == 14592
assert solution.findKthNumber(99, 425, 27497) == 12508
assert solution.findKthNumber(322, 698, 56626) == 15554
assert solution.findKthNumber(354, 574, 110034) == 43401
assert solution.findKthNumber(37, 793, 15036) == 5904
assert solution.findKthNumber(239, 136, 11526) == 3675
assert solution.findKthNumber(991, 374, 163504) == 57200
assert solution.findKthNumber(671, 59, 38362) == 30470
assert solution.findKthNumber(16, 849, 2859) == 848
assert solution.findKthNumber(477, 473, 206000) == 138700
assert solution.findKthNumber(542, 938, 153809) == 45150
assert solution.findKthNumber(923, 887, 55051) == 10434
assert solution.findKthNumber(134, 816, 27522) == 7638
assert solution.findKthNumber(691, 309, 115641) == 45621
assert solution.findKthNumber(277, 31, 7799) == 5301
assert solution.findKthNumber(554, 327, 27529) == 6448
assert solution.findKthNumber(582, 506, 143341) == 52932
assert solution.findKthNumber(759, 86, 38677) == 16354
assert solution.findKthNumber(776, 131, 78374) == 41470
assert solution.findKthNumber(483, 192, 41807) == 14874
assert solution.findKthNumber(755, 250, 73364) == 24150
assert solution.findKthNumber(553, 875, 61028) == 13470
assert solution.findKthNumber(896, 968, 515939) == 216250
assert solution.findKthNumber(759, 481, 278001) == 144434
assert solution.findKthNumber(679, 783, 53612) == 11172