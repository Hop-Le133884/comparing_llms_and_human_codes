
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
    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k % 2

solution=Solution()
assert solution.reachNumber(319697706) == 25287
assert solution.reachNumber(651155756) == 36088
assert solution.reachNumber(-289867697) == 24078
assert solution.reachNumber(42864468) == 9259
assert solution.reachNumber(733236850) == 38295
assert solution.reachNumber(-226060402) == 21263
assert solution.reachNumber(665033385) == 36470
assert solution.reachNumber(-533129817) == 32654
assert solution.reachNumber(278112474) == 23584
assert solution.reachNumber(584932322) == 34203
assert solution.reachNumber(17750403) == 5958
assert solution.reachNumber(361235796) == 26879
assert solution.reachNumber(-730671551) == 38229
assert solution.reachNumber(-195805455) == 19789
assert solution.reachNumber(418723731) == 28941
assert solution.reachNumber(532727281) == 32641
assert solution.reachNumber(138925891) == 16669
assert solution.reachNumber(89967913) == 13414
assert solution.reachNumber(-846676944) == 41151
assert solution.reachNumber(-669377249) == 36589
assert solution.reachNumber(189384403) == 19462
assert solution.reachNumber(883771898) == 42043
assert solution.reachNumber(482314226) == 31059
assert solution.reachNumber(540509846) == 32879
assert solution.reachNumber(-850958974) == 41255
assert solution.reachNumber(-659034535) == 36305
assert solution.reachNumber(11285953) == 4753
assert solution.reachNumber(6187438) == 3519
assert solution.reachNumber(498616040) == 31579
assert solution.reachNumber(1945021) == 1973
assert solution.reachNumber(254550102) == 22563
assert solution.reachNumber(-30650096) == 7831
assert solution.reachNumber(-46054114) == 9599
assert solution.reachNumber(175703053) == 18746
assert solution.reachNumber(-292607750) == 24191
assert solution.reachNumber(974109863) == 44141
assert solution.reachNumber(654699) == 1145
assert solution.reachNumber(-476163577) == 30861
assert solution.reachNumber(965554886) == 43944
assert solution.reachNumber(-76587874) == 12376
assert solution.reachNumber(973345944) == 44123
assert solution.reachNumber(466938420) == 30559
assert solution.reachNumber(274906353) == 23449
assert solution.reachNumber(676655877) == 36789
assert solution.reachNumber(640478405) == 35790
assert solution.reachNumber(-91277180) == 13511
assert solution.reachNumber(644627313) == 35906
assert solution.reachNumber(686253373) == 37049
assert solution.reachNumber(635238872) == 35644
assert solution.reachNumber(-880404602) == 41963
assert solution.reachNumber(-615579030) == 35088
assert solution.reachNumber(94000915) == 13713
assert solution.reachNumber(217881643) == 20877
assert solution.reachNumber(594483847) == 34481
assert solution.reachNumber(-557686823) == 33397
assert solution.reachNumber(917596) == 1355
assert solution.reachNumber(596043379) == 34529
assert solution.reachNumber(759693252) == 38979
assert solution.reachNumber(608907029) == 34897
assert solution.reachNumber(175082265) == 18713
assert solution.reachNumber(860854073) == 41493
assert solution.reachNumber(-602229091) == 34705
assert solution.reachNumber(903029733) == 42498
assert solution.reachNumber(-998158083) == 44681
assert solution.reachNumber(-21079209) == 6493
assert solution.reachNumber(435956127) == 29529
assert solution.reachNumber(606149987) == 34818
assert solution.reachNumber(492320734) == 31379
assert solution.reachNumber(180639937) == 19009
assert solution.reachNumber(-8125250) == 4031
assert solution.reachNumber(-520403622) == 32263
assert solution.reachNumber(586625581) == 34253
assert solution.reachNumber(-759624240) == 38979
assert solution.reachNumber(-741756610) == 38516
assert solution.reachNumber(-958545150) == 43787
assert solution.reachNumber(-720089750) == 37951
assert solution.reachNumber(724169641) == 38057
assert solution.reachNumber(104467038) == 14455
assert solution.reachNumber(-44177869) == 9401
assert solution.reachNumber(124014223) == 15749
assert solution.reachNumber(962740052) == 43880
assert solution.reachNumber(37481585) == 8658
assert solution.reachNumber(534767127) == 32705
assert solution.reachNumber(142679100) == 16895
assert solution.reachNumber(914771661) == 42773
assert solution.reachNumber(-56006065) == 10585
assert solution.reachNumber(756504511) == 38897
assert solution.reachNumber(-525419175) == 32417
assert solution.reachNumber(-988414976) == 44463
assert solution.reachNumber(941346331) == 43390
assert solution.reachNumber(-483288990) == 31091
assert solution.reachNumber(-322315293) == 25390
assert solution.reachNumber(478508339) == 30937
assert solution.reachNumber(-638404900) == 35732
assert solution.reachNumber(470757635) == 30685
assert solution.reachNumber(-439682757) == 29654
assert solution.reachNumber(950363664) == 43599
assert solution.reachNumber(49105848) == 9911
assert solution.reachNumber(893361660) == 42271
assert solution.reachNumber(-874629533) == 41825