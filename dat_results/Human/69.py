
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
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) >> 1
            # mid*mid <= x
            if mid <= x // mid:
                left = mid
            else:
                right = mid - 1
        return left

solution=Solution()
assert solution.mySqrt(1183590127) == 34403
assert solution.mySqrt(614217718) == 24783
assert solution.mySqrt(250407520) == 15824
assert solution.mySqrt(1168930359) == 34189
assert solution.mySqrt(1611111290) == 40138
assert solution.mySqrt(1350239661) == 36745
assert solution.mySqrt(1628456674) == 40354
assert solution.mySqrt(1992105920) == 44633
assert solution.mySqrt(2136663874) == 46224
assert solution.mySqrt(1088576031) == 32993
assert solution.mySqrt(1783567741) == 42232
assert solution.mySqrt(159250475) == 12619
assert solution.mySqrt(1576461795) == 39704
assert solution.mySqrt(137131377) == 11710
assert solution.mySqrt(420550848) == 20507
assert solution.mySqrt(1525935975) == 39063
assert solution.mySqrt(320493364) == 17902
assert solution.mySqrt(601833634) == 24532
assert solution.mySqrt(630360980) == 25106
assert solution.mySqrt(10401807) == 3225
assert solution.mySqrt(1496628740) == 38686
assert solution.mySqrt(1733519687) == 41635
assert solution.mySqrt(381681254) == 19536
assert solution.mySqrt(636042706) == 25219
assert solution.mySqrt(1442049424) == 37974
assert solution.mySqrt(829547011) == 28801
assert solution.mySqrt(1444148583) == 38001
assert solution.mySqrt(1737996237) == 41689
assert solution.mySqrt(1910317693) == 43707
assert solution.mySqrt(1893701716) == 43516
assert solution.mySqrt(1209822274) == 34782
assert solution.mySqrt(89289841) == 9449
assert solution.mySqrt(1953942011) == 44203
assert solution.mySqrt(1213740742) == 34838
assert solution.mySqrt(1633696603) == 40419
assert solution.mySqrt(1402153062) == 37445
assert solution.mySqrt(603160732) == 24559
assert solution.mySqrt(1035304431) == 32176
assert solution.mySqrt(903772431) == 30062
assert solution.mySqrt(1135004164) == 33689
assert solution.mySqrt(1349114178) == 36730
assert solution.mySqrt(472875554) == 21745
assert solution.mySqrt(756817771) == 27510
assert solution.mySqrt(1445100284) == 38014
assert solution.mySqrt(1842204647) == 42920
assert solution.mySqrt(170144962) == 13043
assert solution.mySqrt(1985539448) == 44559
assert solution.mySqrt(1919925469) == 43816
assert solution.mySqrt(1302667914) == 36092
assert solution.mySqrt(1774204938) == 42121
assert solution.mySqrt(384778583) == 19615
assert solution.mySqrt(936738235) == 30606
assert solution.mySqrt(1351629648) == 36764
assert solution.mySqrt(985581667) == 31393
assert solution.mySqrt(202744885) == 14238
assert solution.mySqrt(1151345617) == 33931
assert solution.mySqrt(560168206) == 23667
assert solution.mySqrt(1487166834) == 38563
assert solution.mySqrt(341654557) == 18483
assert solution.mySqrt(1623902505) == 40297
assert solution.mySqrt(1093074807) == 33061
assert solution.mySqrt(1308714980) == 36176
assert solution.mySqrt(1436250084) == 37897
assert solution.mySqrt(605968361) == 24616
assert solution.mySqrt(77703747) == 8814
assert solution.mySqrt(1390631718) == 37291
assert solution.mySqrt(498436944) == 22325
assert solution.mySqrt(86716838) == 9312
assert solution.mySqrt(1493036524) == 38639
assert solution.mySqrt(270324403) == 16441
assert solution.mySqrt(1006742623) == 31729
assert solution.mySqrt(1548675749) == 39353
assert solution.mySqrt(2064821221) == 45440
assert solution.mySqrt(1180922888) == 34364
assert solution.mySqrt(438922532) == 20950
assert solution.mySqrt(420966498) == 20517
assert solution.mySqrt(1179872935) == 34349
assert solution.mySqrt(358997629) == 18947
assert solution.mySqrt(1165772933) == 34143
assert solution.mySqrt(386673635) == 19664
assert solution.mySqrt(1915889437) == 43770
assert solution.mySqrt(1193487850) == 34546
assert solution.mySqrt(276356969) == 16623
assert solution.mySqrt(1462729143) == 38245
assert solution.mySqrt(1458872457) == 38195
assert solution.mySqrt(970781975) == 31157
assert solution.mySqrt(126475687) == 11246
assert solution.mySqrt(61213967) == 7823
assert solution.mySqrt(644859513) == 25394
assert solution.mySqrt(825271117) == 28727
assert solution.mySqrt(1740691448) == 41721
assert solution.mySqrt(698494359) == 26429
assert solution.mySqrt(1944586200) == 44097
assert solution.mySqrt(1944051829) == 44091
assert solution.mySqrt(1074848229) == 32784
assert solution.mySqrt(1653255891) == 40660
assert solution.mySqrt(669465594) == 25874
assert solution.mySqrt(1571549601) == 39642
assert solution.mySqrt(1207036865) == 34742
assert solution.mySqrt(494428693) == 22235