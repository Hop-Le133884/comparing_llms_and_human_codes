
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
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] - mid - 1 >= k:
                right = mid
            else:
                left = mid + 1
        return arr[left - 1] + k - (arr[left - 1] - (left - 1) - 1)

solution=Solution()
assert solution.findKthPositive([80, 114, 249, 442, 555, 644, 665, 747, 869], 494) == 498
assert solution.findKthPositive([321, 329, 384, 431, 443, 580], 977) == 983
assert solution.findKthPositive([86, 163, 342, 351, 583, 704, 713, 739, 876, 906], 139) == 140
assert solution.findKthPositive([6, 163, 191, 298, 355, 811, 830, 905, 919], 739) == 744
assert solution.findKthPositive([760, 837, 934, 949], 605) == 605
assert solution.findKthPositive([989], 189) == 189
assert solution.findKthPositive([53], 472) == 473
assert solution.findKthPositive([67, 152, 240, 299, 417, 520, 650, 717, 740], 499) == 504
assert solution.findKthPositive([337, 384, 456, 557], 419) == 421
assert solution.findKthPositive([10, 54, 257, 424, 700, 904, 931], 466) == 470
assert solution.findKthPositive([30, 389], 882) == 884
assert solution.findKthPositive([134, 424, 545, 569, 917], 502) == 504
assert solution.findKthPositive([63, 153, 210, 371, 435, 589, 648, 767, 783], 102) == 103
assert solution.findKthPositive([203, 262, 772, 910, 915, 991], 342) == 344
assert solution.findKthPositive([14, 98, 217, 381, 555, 643, 673, 780, 992], 36) == 37
assert solution.findKthPositive([2, 147, 253, 299, 396, 522, 527, 833, 854, 874], 288) == 291
assert solution.findKthPositive([149, 327, 583, 610, 773, 796, 822], 259) == 260
assert solution.findKthPositive([326, 512, 618, 693], 507) == 508
assert solution.findKthPositive([386, 445], 744) == 746
assert solution.findKthPositive([156, 241, 300, 445, 523, 565, 598, 804, 811, 844], 730) == 737
assert solution.findKthPositive([126, 621, 675, 704, 803, 856, 921], 721) == 725
assert solution.findKthPositive([51, 180, 207, 350, 416, 555], 987) == 993
assert solution.findKthPositive([49, 61, 677, 803, 883], 120) == 122
assert solution.findKthPositive([148, 334, 473, 474, 664, 667, 754, 869, 966], 873) == 881
assert solution.findKthPositive([24, 30, 86, 396, 423, 481, 537, 955, 997], 134) == 137
assert solution.findKthPositive([51, 112, 255, 268, 547, 628, 888], 331) == 335
assert solution.findKthPositive([13, 16, 25, 54, 64, 73, 85, 618, 645, 810], 133) == 140
assert solution.findKthPositive([331, 387, 738, 904], 948) == 952
assert solution.findKthPositive([12, 390, 452, 520, 543, 565, 690, 973], 160) == 161
assert solution.findKthPositive([162, 221, 380, 543, 834, 926, 995], 789) == 793
assert solution.findKthPositive([120, 319, 394, 405, 446, 530, 569, 598, 699, 986], 133) == 134
assert solution.findKthPositive([110, 122, 643, 669, 768, 860, 884, 983], 409) == 411
assert solution.findKthPositive([116, 312, 410, 459, 691, 728, 849, 977], 569) == 573
assert solution.findKthPositive([123, 272, 426, 528, 557, 558, 617, 806, 854], 310) == 312
assert solution.findKthPositive([767], 499) == 499
assert solution.findKthPositive([213, 279, 339, 402, 470, 732, 969], 502) == 507
assert solution.findKthPositive([165, 167, 720, 787, 936], 1000) == 1005
assert solution.findKthPositive([41, 92, 192, 296, 333, 460, 577, 700, 755, 868], 283) == 286
assert solution.findKthPositive([143, 347, 976], 956) == 958
assert solution.findKthPositive([250, 314, 360, 485, 510, 578, 636, 816, 973], 805) == 812
assert solution.findKthPositive([50, 385, 409, 678, 787], 60) == 61
assert solution.findKthPositive([77, 210, 213, 688], 910) == 914
assert solution.findKthPositive([344, 451, 801, 805, 883, 939, 992], 810) == 814
assert solution.findKthPositive([339, 428, 477, 512, 954, 977], 594) == 598
assert solution.findKthPositive([373, 587, 858], 571) == 572
assert solution.findKthPositive([22, 30, 91, 223, 531, 575, 646, 786, 988], 916) == 924
assert solution.findKthPositive([925], 88) == 88
assert solution.findKthPositive([785], 931) == 932
assert solution.findKthPositive([124, 256, 379, 433, 434, 510, 661, 704, 710], 116) == 116
assert solution.findKthPositive([71, 753], 736) == 737
assert solution.findKthPositive([103, 120, 493, 519, 572, 638, 668, 938], 882) == 889
assert solution.findKthPositive([336, 809], 280) == 280
assert solution.findKthPositive([6, 30, 320, 379, 483, 700, 778, 883], 928) == 936
assert solution.findKthPositive([152, 221, 270, 471, 720, 748, 847, 887, 969], 351) == 354
assert solution.findKthPositive([182, 220, 376, 393, 454, 787, 847, 940], 856) == 863
assert solution.findKthPositive([139], 321) == 322
assert solution.findKthPositive([12, 42, 97, 161, 297, 443, 446, 542, 593, 885], 832) == 841
assert solution.findKthPositive([178, 318, 493, 532, 564, 952], 52) == 52
assert solution.findKthPositive([374, 664], 739) == 741
assert solution.findKthPositive([58, 414, 871], 161) == 162
assert solution.findKthPositive([97, 128, 202, 231, 280, 499, 544, 602, 860], 991) == 1000
assert solution.findKthPositive([52, 78, 82, 145, 443, 592, 691, 943], 128) == 131
assert solution.findKthPositive([174, 244, 336], 572) == 575
assert solution.findKthPositive([102, 180, 188, 252, 623, 778], 868) == 874
assert solution.findKthPositive([34, 157, 294, 320, 326, 554, 742, 910, 921], 556) == 562
assert solution.findKthPositive([210, 471], 298) == 299
assert solution.findKthPositive([806], 89) == 89
assert solution.findKthPositive([244, 651, 837, 870], 801) == 803
assert solution.findKthPositive([53, 222, 492, 755, 852, 964], 133) == 134
assert solution.findKthPositive([123, 240, 287, 346, 365, 407, 527, 623, 910], 450) == 456
assert solution.findKthPositive([209, 242, 786], 805) == 808
assert solution.findKthPositive([53, 84, 165, 714, 978], 604) == 607
assert solution.findKthPositive([575, 889], 87) == 87
assert solution.findKthPositive([295, 524, 794], 688) == 690
assert solution.findKthPositive([25, 153, 367, 601, 750, 808, 949], 967) == 974
assert solution.findKthPositive([23, 143, 352, 380, 549, 592, 637, 911, 968], 441) == 445
assert solution.findKthPositive([65, 436, 513, 521, 786], 185) == 186
assert solution.findKthPositive([294, 390, 787], 67) == 67
assert solution.findKthPositive([77, 262, 576, 692, 950], 965) == 970
assert solution.findKthPositive([485, 491, 757, 807, 875, 910, 995], 431) == 431
assert solution.findKthPositive([48, 155, 341, 396, 433, 702, 795, 919, 924, 957], 915) == 923
assert solution.findKthPositive([168, 279, 540, 627], 95) == 95
assert solution.findKthPositive([15, 32, 286, 355, 399, 431, 511, 880, 896, 983], 123) == 125
assert solution.findKthPositive([17, 55, 190, 220, 480, 548, 902, 910, 911, 912], 134) == 136
assert solution.findKthPositive([489, 603, 718], 413) == 413
assert solution.findKthPositive([210, 236, 261, 397, 541, 628, 908, 983], 28) == 28
assert solution.findKthPositive([246, 653], 473) == 474
assert solution.findKthPositive([44, 158, 316, 360, 417, 478], 409) == 413
assert solution.findKthPositive([121, 127, 254, 404, 628, 641, 763, 796, 991], 944) == 952
assert solution.findKthPositive([227, 247, 280, 311, 319, 570, 596, 799, 984], 375) == 380
assert solution.findKthPositive([79, 296, 517, 544, 562, 569, 571, 830, 884, 907], 316) == 318
assert solution.findKthPositive([46, 93, 187, 388, 553, 755, 769], 79) == 80
assert solution.findKthPositive([113], 667) == 668
assert solution.findKthPositive([142, 416, 580, 668, 726, 821, 896, 908], 173) == 174
assert solution.findKthPositive([110, 155, 185, 283, 479, 524, 608, 814, 914, 944], 909) == 918
assert solution.findKthPositive([81, 133, 461], 468) == 471
assert solution.findKthPositive([237, 919], 24) == 24
assert solution.findKthPositive([432, 637], 983) == 985
assert solution.findKthPositive([170, 326, 376, 504, 672, 822, 982], 794) == 799
assert solution.findKthPositive([216], 730) == 731