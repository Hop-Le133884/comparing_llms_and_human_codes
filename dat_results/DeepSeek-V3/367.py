
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
    def isPerfectSquare(self, num):
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

solution=Solution()
assert solution.isPerfectSquare(198794985) == False
assert solution.isPerfectSquare(720548389) == False
assert solution.isPerfectSquare(250143627) == False
assert solution.isPerfectSquare(365152663) == False
assert solution.isPerfectSquare(538451209) == False
assert solution.isPerfectSquare(115641585) == False
assert solution.isPerfectSquare(959452724) == False
assert solution.isPerfectSquare(479537366) == False
assert solution.isPerfectSquare(744827671) == False
assert solution.isPerfectSquare(944380383) == False
assert solution.isPerfectSquare(238832600) == False
assert solution.isPerfectSquare(342262367) == False
assert solution.isPerfectSquare(483222743) == False
assert solution.isPerfectSquare(499687912) == False
assert solution.isPerfectSquare(841912817) == False
assert solution.isPerfectSquare(482272714) == False
assert solution.isPerfectSquare(703251589) == False
assert solution.isPerfectSquare(934847989) == False
assert solution.isPerfectSquare(669698720) == False
assert solution.isPerfectSquare(830608478) == False
assert solution.isPerfectSquare(248581709) == False
assert solution.isPerfectSquare(263563987) == False
assert solution.isPerfectSquare(942476260) == False
assert solution.isPerfectSquare(157878280) == False
assert solution.isPerfectSquare(725797610) == False
assert solution.isPerfectSquare(13540181) == False
assert solution.isPerfectSquare(597374276) == False
assert solution.isPerfectSquare(703627172) == False
assert solution.isPerfectSquare(768222469) == False
assert solution.isPerfectSquare(668430690) == False
assert solution.isPerfectSquare(294394462) == False
assert solution.isPerfectSquare(930381796) == False
assert solution.isPerfectSquare(726722485) == False
assert solution.isPerfectSquare(503953295) == False
assert solution.isPerfectSquare(971482225) == False
assert solution.isPerfectSquare(52053180) == False
assert solution.isPerfectSquare(766362144) == False
assert solution.isPerfectSquare(781002220) == False
assert solution.isPerfectSquare(340631018) == False
assert solution.isPerfectSquare(537443608) == False
assert solution.isPerfectSquare(539489749) == False
assert solution.isPerfectSquare(60405520) == False
assert solution.isPerfectSquare(602748631) == False
assert solution.isPerfectSquare(489146447) == False
assert solution.isPerfectSquare(192651032) == False
assert solution.isPerfectSquare(493806312) == False
assert solution.isPerfectSquare(44403405) == False
assert solution.isPerfectSquare(857988568) == False
assert solution.isPerfectSquare(735480287) == False
assert solution.isPerfectSquare(301167671) == False
assert solution.isPerfectSquare(615862794) == False
assert solution.isPerfectSquare(81193619) == False
assert solution.isPerfectSquare(370617581) == False
assert solution.isPerfectSquare(117424212) == False
assert solution.isPerfectSquare(569135555) == False
assert solution.isPerfectSquare(565342110) == False
assert solution.isPerfectSquare(696794818) == False
assert solution.isPerfectSquare(39621729) == False
assert solution.isPerfectSquare(833090427) == False
assert solution.isPerfectSquare(775341633) == False
assert solution.isPerfectSquare(675641242) == False
assert solution.isPerfectSquare(120275584) == False
assert solution.isPerfectSquare(359521544) == False
assert solution.isPerfectSquare(81575597) == False
assert solution.isPerfectSquare(630752819) == False
assert solution.isPerfectSquare(842657369) == False
assert solution.isPerfectSquare(932591914) == False
assert solution.isPerfectSquare(329543741) == False
assert solution.isPerfectSquare(356702622) == False
assert solution.isPerfectSquare(681621452) == False
assert solution.isPerfectSquare(857335319) == False
assert solution.isPerfectSquare(820883392) == False
assert solution.isPerfectSquare(275867257) == False
assert solution.isPerfectSquare(628566156) == False
assert solution.isPerfectSquare(616478052) == False
assert solution.isPerfectSquare(930567440) == False
assert solution.isPerfectSquare(181748619) == False
assert solution.isPerfectSquare(716617557) == False
assert solution.isPerfectSquare(514385759) == False
assert solution.isPerfectSquare(465711156) == False
assert solution.isPerfectSquare(903168362) == False
assert solution.isPerfectSquare(988819828) == False
assert solution.isPerfectSquare(355881984) == False
assert solution.isPerfectSquare(998741404) == False
assert solution.isPerfectSquare(74830554) == False
assert solution.isPerfectSquare(326906156) == False
assert solution.isPerfectSquare(301642505) == False
assert solution.isPerfectSquare(818181804) == False
assert solution.isPerfectSquare(69679267) == False
assert solution.isPerfectSquare(797640331) == False
assert solution.isPerfectSquare(158698972) == False
assert solution.isPerfectSquare(79299359) == False
assert solution.isPerfectSquare(211169605) == False
assert solution.isPerfectSquare(807518849) == False
assert solution.isPerfectSquare(790808220) == False
assert solution.isPerfectSquare(940414795) == False
assert solution.isPerfectSquare(548763556) == False
assert solution.isPerfectSquare(883405399) == False
assert solution.isPerfectSquare(490152894) == False
assert solution.isPerfectSquare(433853965) == False