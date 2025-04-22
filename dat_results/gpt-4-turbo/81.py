
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
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Skip duplicates from the left
            while left < mid and nums[left] == nums[mid]:
                left += 1
            # Skip duplicates from the right
            while right > mid and nums[right] == nums[mid]:
                right -= 1

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


solution=Solution()
assert solution.search([-9291, -1385], 7240) == False
assert solution.search([-8954, -8049, -7190, -2609, -382, 609, 5612, 6601, 8155], -8472) == False
assert solution.search([-6379, -4501, -1283, 325, 5728, 5823, 7194, 7221], -7012) == False
assert solution.search([-8672, -6987, -1908, 312, 658, 3573, 4770], -2400) == False
assert solution.search([-9641, -4751, -3099, -1804, -1255, 2287, 4166], -3608) == False
assert solution.search([-5954, -2108, 5357, 5443], -7450) == False
assert solution.search([-8637, -8052, -4351, -2411, -1809, 986, 3731, 6794], -3397) == False
assert solution.search([-9793, -1351, -252, 3068, 4484], 1923) == False
assert solution.search([-8044, -6003, -3837, -1905, 1596, 4310, 4810, 7633, 8151], -8753) == False
assert solution.search([-7230, -3044, -1756, 1047, 7140], 6685) == False
assert solution.search([-9895, -7366, -7292, -2695, -262, 7820, 8388], -6292) == False
assert solution.search([-7771, 6350, 8466], 7538) == False
assert solution.search([-3555, 2745], 6697) == False
assert solution.search([-6318, -5721, -5302, 4096], -3828) == False
assert solution.search([-3962, 4175, 7493, 8660], 5521) == False
assert solution.search([-2703, -823, -630, 1947, 2055, 7419], -8545) == False
assert solution.search([-5704, -5322, -2428, 1806, 2229, 4564], -7662) == False
assert solution.search([-8826, -8796, -8006, -7565, -1868, 3231, 6483, 6819, 6838], 5711) == False
assert solution.search([-9494, -5525, 160, 379], 4969) == False
assert solution.search([-4801, -2179, -1718, 2095, 5261, 8785], -1929) == False
assert solution.search([1419, 2980, 4056], 7051) == False
assert solution.search([-2584, 6948], -2203) == False
assert solution.search([-9829, -6938, -6676, -6498, -2815, 1644, 2415, 5913, 7838], 7805) == False
assert solution.search([-9089, -7608, -5578, -3833, -3540, -2618, -481, 2354, 4631, 8006], -9726) == False
assert solution.search([-5928, -5873, -2952, -1017, -146, 2303, 5630, 7705, 7851], 561) == False
assert solution.search([-6798, -5128, -2029, 3644, 4805], 2729) == False
assert solution.search([7067, 8916], -8265) == False
assert solution.search([-4451, -654, 1731, 9330, 9513], 4035) == False
assert solution.search([-8052, -5888, -2861, -801, 1765, 2446, 7222, 7371], -5115) == False
assert solution.search([-9324, -7753, -7212, -6087, -4254, 2885, 3449], -1659) == False
assert solution.search([-6638, -1852, -1540, 1421, 1684, 3116, 4691, 6537, 9228], 4375) == False
assert solution.search([-7843, -5568, -3791], 9691) == False
assert solution.search([-3042, 8852], 797) == False
assert solution.search([-6234, -5978, -4172, -272, 3523, 5676], -7478) == False
assert solution.search([-8030, -6853, -5456, -4282, -1337, -1217, -886, 3508, 3816, 8404], 6086) == False
assert solution.search([2988, 3230, 5651, 6599], 8273) == False
assert solution.search([5586], -6543) == False
assert solution.search([-6781, -2736, 119, 937, 1310, 1385, 1868, 2102, 2755], -8688) == False
assert solution.search([-9888, -4900, -4390, 30, 6445, 6693, 7377], -5271) == False
assert solution.search([-2312, -1859, -1507, -1449, 1282, 2068, 6931, 7407], -4177) == False
assert solution.search([-8240, -3712, -1499, 250, 5823], 730) == False
assert solution.search([-6728, -6717, -3352, -2160, 5942, 9584], 7649) == False
assert solution.search([-5590, -5462, -1662, 294, 3394], -1583) == False
assert solution.search([-8055, -5024, -3601, 774, 3776, 7393, 8294, 9606], 7731) == False
assert solution.search([-7723, -5195, 5184], -976) == False
assert solution.search([-7251, -5123, -2293, 627, 652, 4551, 4837, 4881, 9585], 2070) == False
assert solution.search([-7529, -4903, -4217, 7756, 9401], -8825) == False
assert solution.search([-9310, -7978, -2466, 1366, 4229, 9399, 9673], -9409) == False
assert solution.search([-3517, -2501, -1297, -699, 3535, 7001, 9511], 9824) == False
assert solution.search([-2256, -1928, -1003, 5626, 7061, 8032, 8102, 9891], 7418) == False
assert solution.search([-8438, -4432, -4392, -421, 2800, 9201], -9469) == False
assert solution.search([-5028, 793, 1863, 2029, 3958, 4536, 7595], 3884) == False
assert solution.search([-5452, 2088, 2419], 51) == False
assert solution.search([-9418, -5873, -4121, 4575, 7609, 8823], -3944) == False
assert solution.search([-9884, 2398, 8110], -6452) == False
assert solution.search([-9713, -8365, -3512, -2992, 4368], 7424) == False
assert solution.search([-7083, -6444, 456, 2360, 3560, 8807], -3471) == False
assert solution.search([-7793, -5521, -4219, -2892, 1008, 1036, 2298, 2867, 3985, 8923], -9424) == False
assert solution.search([-4382, -1582, -1184, 4851], -2639) == False
assert solution.search([-9604, -7596, -4733, -3445, -3350, 609, 2030, 3050, 4392, 9591], -8386) == False
assert solution.search([-9900], 6819) == False
assert solution.search([-9585, -4800, -3928, -1343, -595, -266, 1973, 5879, 6213, 6868], 290) == False
assert solution.search([-5128, -3324, -3228], -9755) == False
assert solution.search([-580, 1881, 4107, 5039, 7445, 7983, 8913, 9529], 1424) == False
assert solution.search([-9104, -8612, -6746, -5758, -5038, 799, 7597], -2584) == False
assert solution.search([-4793, -2666, 2333, 2365], 5187) == False
assert solution.search([1481, 3037, 3365, 3793], -3839) == False
assert solution.search([-7378, -6874, -4939, -3635, -2613, -1361, 1114, 6228, 9386], 1044) == False
assert solution.search([-6304, -5714, -5061, -3191, -184, 1691, 1723, 3834, 4241], 9857) == False
assert solution.search([-9474, -7605, -5541, -4530, -4008, -2510, -122, 1581], 3033) == False
assert solution.search([-4442, -2633, 4340, 5686, 7454, 9064], -7475) == False
assert solution.search([-6565, -1218, 762, 2420, 3632, 6175, 9906], 2171) == False
assert solution.search([-8121, -6994, -4908, -4065, -3015, -565, -190, 1435], 6856) == False
assert solution.search([-8971, -4185, 460, 6954, 7160, 7963], 2148) == False
assert solution.search([-7042, -4715, 6789, 8985], 6047) == False
assert solution.search([-9751, -3280, 2046], 7634) == False
assert solution.search([-8600, -7730, -4923, -2312, -1422, 535, 1768, 2688, 3851, 7149], -8261) == False
assert solution.search([1214], 5519) == False
assert solution.search([92, 6101], -1046) == False
assert solution.search([-8454, -7102, -3336, -1479, -10, 8786], -3936) == False
assert solution.search([-9380, -8526, -7160, -6678, -833, 1726, 1810], 9524) == False
assert solution.search([-6650, -4800, -583, 928, 8380, 8388], -3831) == False
assert solution.search([917, 1039, 7682], 4960) == False
assert solution.search([4319], -81) == False
assert solution.search([-9481, -8381, -280, 7608, 7659], -3530) == False
assert solution.search([-8040], 3253) == False
assert solution.search([-9067, -3762, -3470, -938, -161, -137, 974, 3818, 6228, 9188], -9494) == False
assert solution.search([-8681, -8554, 841, 3432], -6420) == False
assert solution.search([-3785, 7528], 5120) == False
assert solution.search([-6227, -5750, -4070, 1197, 6265], -6059) == False
assert solution.search([-7170, -3100, -2239, 98, 2134, 9184], 7278) == False
assert solution.search([-2732, -2054, 4963, 5400, 5730], 6804) == False
assert solution.search([-9465, -3594, 73], -2147) == False
assert solution.search([-7387, -2836, -2619, -1640, -958, -373, 1235, 1757, 4479], -1417) == False
assert solution.search([-9044, -7651, -6712, 4579, 5853, 9561], 7118) == False
assert solution.search([-9927, 5893], 8014) == False
assert solution.search([-295, 8674, 8970], -107) == False
assert solution.search([-7160, -4009, -3474, -3264, 2059, 6182, 7502, 7599, 8311, 8722], -1283) == False
assert solution.search([-9836, 451, 4263, 7847], 6010) == False
assert solution.search([9538], -1576) == False