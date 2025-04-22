
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
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        cnt = Counter(arr1 + arr2 + arr3)
        return [x for x in arr1 if cnt[x] == 3]

solution=Solution()
assert solution.arraysIntersection([794, 556, 528, 215, 852, 839], [180, 690, 961, 770], [567, 927]) == []
assert solution.arraysIntersection([251, 258, 172, 971, 518, 907, 436, 605, 666, 932], [764, 426, 318, 182, 29, 612, 747, 999], [480, 883, 110, 798, 598, 210]) == []
assert solution.arraysIntersection([844, 127, 776, 314, 681, 632, 529], [202, 718, 67, 815, 851, 500], [86, 942, 294, 549]) == []
assert solution.arraysIntersection([251, 887, 956, 405, 320, 935, 873, 483, 485], [912, 762, 890], [174, 127, 399, 13]) == []
assert solution.arraysIntersection([377, 872, 354, 220, 519], [349, 807, 195, 668, 42, 341, 891, 286, 383], [842, 474]) == []
assert solution.arraysIntersection([52], [640, 18, 417, 158, 810, 813, 83, 49, 697], [490, 485, 981, 725, 300, 117]) == []
assert solution.arraysIntersection([156, 226], [828, 410, 472, 895, 341, 411, 212], [398, 785, 295, 280]) == []
assert solution.arraysIntersection([576, 101, 22, 954, 359, 823, 581, 328, 874], [712, 439, 132, 963, 277], [108, 429, 220]) == []
assert solution.arraysIntersection([15, 373, 393], [98, 441, 642, 383, 227, 511, 68, 999, 741, 512], [723]) == []
assert solution.arraysIntersection([824, 669, 362, 671, 852, 840], [351, 285, 746, 17, 114, 638, 70, 927], [562]) == []
assert solution.arraysIntersection([218, 494], [911, 434, 462, 26, 995, 996, 579], [776, 644, 245, 373, 364, 536, 759, 318, 744]) == []
assert solution.arraysIntersection([938, 912, 631], [984, 514, 236, 693, 508, 850, 189, 988, 865, 739], [49]) == []
assert solution.arraysIntersection([908, 104, 613, 904, 334, 170, 423], [31, 597, 29, 658, 592, 215], [74, 422]) == []
assert solution.arraysIntersection([265, 282, 398, 232, 97, 473, 838], [768, 771, 821], [688, 713, 180, 657, 665, 642, 130, 29, 314, 831]) == []
assert solution.arraysIntersection([211, 500, 553, 820, 332, 325, 18, 360, 800, 87], [266, 258, 290, 574, 540, 947, 565, 369, 869], [916, 199, 466, 600, 316, 709, 570, 1000, 680]) == []
assert solution.arraysIntersection([779, 420], [97, 153, 13, 830, 531, 342, 762], [554, 263, 625, 738, 339, 776, 528, 727, 169]) == []
assert solution.arraysIntersection([924], [190, 393, 135, 392, 512, 8], [562, 38, 631, 605, 571, 299, 53]) == []
assert solution.arraysIntersection([236, 862, 54, 930, 595, 480, 385, 981, 860, 389], [480, 904, 822, 913, 210, 349, 978, 543, 115], [399, 381, 600, 207, 567, 553, 298, 92, 597, 325]) == []
assert solution.arraysIntersection([623, 473, 841, 464, 313, 656, 43, 11], [614, 106, 800, 644, 275, 282, 599, 377], [857, 401, 767]) == []
assert solution.arraysIntersection([565, 161], [321, 407, 112, 812, 122], [796, 527]) == []
assert solution.arraysIntersection([905, 948, 579, 974], [746, 204, 619, 766, 153, 92], [776, 195, 823, 987, 998, 589, 437, 79, 478, 198]) == []
assert solution.arraysIntersection([616, 451, 113, 64, 125, 230, 720, 139, 438, 356], [983, 557], [371, 968, 753, 825]) == []
assert solution.arraysIntersection([75, 59, 589, 430, 35, 880, 452], [388, 583, 995, 396, 495, 133, 642, 718], [58, 788, 820, 187, 712, 903, 72, 999, 917, 629]) == []
assert solution.arraysIntersection([753, 720], [823], [70, 177, 96, 589, 390, 626, 649, 931]) == []
assert solution.arraysIntersection([773, 453, 515, 722, 618, 885, 474], [975, 324, 384, 930, 88, 128, 379, 172, 593, 97], [107, 183, 877, 564, 990]) == []
assert solution.arraysIntersection([49, 315, 619, 116, 676, 843], [244, 444], [428, 394, 945, 388, 289, 448, 969]) == []
assert solution.arraysIntersection([325, 694, 362, 546, 197, 41, 211, 687, 278], [628, 85, 527, 775, 886, 33, 837, 379, 34, 270], [279, 470, 70]) == []
assert solution.arraysIntersection([123, 794, 548, 131, 176, 816, 555], [116, 986, 846, 735, 719, 202, 232, 435, 327, 205], [191, 189, 608, 391, 622, 502, 650]) == []
assert solution.arraysIntersection([504], [84, 430, 917, 454, 487, 218, 789, 618, 355], [731, 792, 649, 36, 289, 706, 794, 880]) == []
assert solution.arraysIntersection([938, 115, 355], [4, 609, 113, 126, 411, 25, 459, 816, 887], [169, 898, 983, 18, 141, 328, 370, 777, 235, 293]) == []
assert solution.arraysIntersection([995, 215, 104, 556, 472, 306, 227, 618], [867, 746, 453, 918], [28, 146, 691]) == []
assert solution.arraysIntersection([187, 887, 644, 515, 923, 892, 480, 97], [211, 911], [699, 312, 572, 379, 452]) == []
assert solution.arraysIntersection([911, 535, 742, 319], [41, 707, 12, 130], [787, 905]) == []
assert solution.arraysIntersection([454, 755, 207, 148, 509, 682, 437, 871, 403, 776], [458, 263, 169, 848], [518, 764, 89, 323, 966, 627, 367, 900, 770]) == []
assert solution.arraysIntersection([260, 151, 841, 703, 624, 326, 612, 510], [305, 34], [552, 59, 352, 107, 869, 66]) == []
assert solution.arraysIntersection([685, 299, 480, 242], [45, 193, 373, 963, 679, 186, 993, 807, 779, 987], [506, 995, 297, 726, 160, 73, 927, 143]) == []
assert solution.arraysIntersection([882, 622, 922, 327, 677, 806, 805, 483, 385], [683, 262, 438, 26], [801, 765, 813, 903, 298, 597, 635, 778]) == []
assert solution.arraysIntersection([339, 452, 935, 81], [33, 554, 615, 946], [546, 861]) == []
assert solution.arraysIntersection([113, 810, 330, 190, 896, 198, 267, 9, 872, 823], [821, 717, 307, 103, 155, 256], [735]) == []
assert solution.arraysIntersection([28, 114, 203, 927, 987, 503, 572, 906, 592], [639, 916, 66, 898, 798, 133, 712, 287, 772], [906, 501, 880, 478, 250, 894, 35]) == []
assert solution.arraysIntersection([375, 404], [268, 611, 14, 445, 312, 925, 667, 236, 995], [74, 749, 197]) == []
assert solution.arraysIntersection([839, 229, 961, 917, 656, 642, 615, 710], [309], [812, 519]) == []
assert solution.arraysIntersection([106], [974, 555, 202, 18, 908, 354, 862, 308, 339], [727, 492, 530, 91, 273, 68]) == []
assert solution.arraysIntersection([425, 249, 980], [995, 425, 325, 60, 514, 198, 224, 67, 728], [86, 625]) == []
assert solution.arraysIntersection([48, 156], [472, 66, 467, 177, 31, 646, 476], [531, 182, 925, 1, 859, 958, 87]) == []
assert solution.arraysIntersection([297, 339, 574, 952, 189, 129, 372, 919], [850, 879], [551, 182, 139, 497, 829, 488, 990, 74, 296, 935]) == []
assert solution.arraysIntersection([557], [425, 743, 138, 527, 255, 264, 466, 172, 747], [32, 346, 339, 899]) == []
assert solution.arraysIntersection([259], [797, 117, 406], [34, 314, 831, 528, 8]) == []
assert solution.arraysIntersection([136], [659], [187, 663, 303]) == []
assert solution.arraysIntersection([105, 633, 483], [806, 931, 224, 897, 616, 401, 158, 504, 200], [700, 518, 547, 573, 540, 198]) == []
assert solution.arraysIntersection([216], [787, 37, 283, 223, 486, 803, 178, 451, 824, 740], [297, 314, 192, 102]) == []
assert solution.arraysIntersection([246, 84, 443, 275], [10, 298, 38, 631], [357, 478, 737, 453, 734, 397, 47]) == []
assert solution.arraysIntersection([921, 123, 153, 2, 316, 212], [739], [404, 213, 856, 512, 977, 192, 542, 445]) == []
assert solution.arraysIntersection([437, 715, 293, 949, 130, 442, 642, 291, 13, 996], [130, 545, 350, 532], [31, 83, 715, 12, 701, 88, 129]) == []
assert solution.arraysIntersection([242, 68, 598, 907, 949], [824, 977, 272, 336, 801, 443], [900, 180, 647]) == []
assert solution.arraysIntersection([792, 931, 14, 563, 125, 581], [473, 126], [973]) == []
assert solution.arraysIntersection([147], [58, 488, 636, 876, 362, 999, 626, 215], [744, 86, 109, 333, 3]) == []
assert solution.arraysIntersection([800, 400, 617, 912, 811, 577, 995, 992, 478], [884, 242, 170, 984, 943, 207, 679, 789, 522, 17], [107]) == []
assert solution.arraysIntersection([999, 542, 653, 760, 19, 218, 36, 634, 728, 141], [287, 298, 681, 582, 852, 315, 479, 419, 848], [862, 533, 32]) == []
assert solution.arraysIntersection([667, 70, 5, 553, 828, 484, 741, 736, 909, 465], [765, 604, 887, 185, 949, 606, 797], [952, 305, 15, 588, 315, 720, 339, 562]) == []
assert solution.arraysIntersection([590, 229, 239, 931, 31, 548, 102, 444, 926], [529, 383, 714, 172, 499], [842, 389, 773, 211, 764, 154, 460]) == []
assert solution.arraysIntersection([350], [453, 48], [834, 464, 546, 112, 884, 310, 164, 199]) == []
assert solution.arraysIntersection([122], [698, 814, 957, 133, 553, 42, 417], [216]) == []
assert solution.arraysIntersection([538, 823, 897, 431, 151, 619], [787, 768], [83, 189, 739, 522, 439, 867, 402]) == []
assert solution.arraysIntersection([246, 919, 101, 306, 226], [815, 592, 835, 173, 251, 962], [655, 528, 914, 58, 840, 586, 317, 298, 553, 209]) == []
assert solution.arraysIntersection([33, 740, 734, 324, 915], [965, 178, 468, 652], [83]) == []
assert solution.arraysIntersection([478, 509, 260, 111, 266, 116, 685, 548, 849, 840], [576, 10], [559, 844, 322, 849]) == []
assert solution.arraysIntersection([408, 832, 862, 246, 989, 199, 783, 842, 875, 673], [201, 31, 722, 6, 538], [921, 801, 418, 42, 90, 293]) == []
assert solution.arraysIntersection([990, 74, 346, 309, 773, 903, 85, 635, 897, 253], [187, 22, 44, 58, 688, 597, 691, 874, 838, 906], [284, 877, 91, 464, 766, 179, 771, 957, 387]) == []
assert solution.arraysIntersection([991, 900, 196, 749], [473], [675, 538, 131, 384, 892, 735]) == []
assert solution.arraysIntersection([626, 197, 308, 633, 536, 192, 838, 179], [467], [80, 364, 529]) == []
assert solution.arraysIntersection([68, 888, 180, 478], [903, 163, 537, 693], [466, 69, 585, 4, 450, 868]) == []
assert solution.arraysIntersection([202, 738, 792, 557, 405, 652, 633, 933, 928], [687], [419, 867, 446, 939, 902, 917, 578]) == []
assert solution.arraysIntersection([321, 109, 711, 548, 201, 285, 939, 114, 714], [663, 711, 702, 252, 181], [918, 519, 440, 281, 155, 569, 169]) == []
assert solution.arraysIntersection([80, 248], [473, 353, 608, 963, 996, 203, 435, 315], [448, 116, 966, 616, 2, 23, 866, 843]) == []
assert solution.arraysIntersection([328, 868, 630, 805, 543, 957, 740, 951], [936, 818, 614, 211, 481, 646, 168, 523, 286, 384], [623, 301]) == []
assert solution.arraysIntersection([275, 26], [851, 735, 534, 645, 188, 726, 334, 259, 511], [793, 180, 371, 352]) == []
assert solution.arraysIntersection([26, 315, 87, 783, 320, 41, 164, 345, 347], [273, 739, 612, 87], [24, 740, 537, 817, 622, 204]) == []
assert solution.arraysIntersection([300, 659, 787, 47, 790, 724, 864], [457, 708, 301, 642, 818, 881, 754], [721, 857, 551, 187, 668, 496, 612, 341, 17]) == []
assert solution.arraysIntersection([714], [671, 499, 521, 77, 434], [193, 350]) == []
assert solution.arraysIntersection([500], [430, 390, 519, 411, 547, 620], [822, 471, 299, 897, 177, 754, 27, 881, 254]) == []
assert solution.arraysIntersection([80, 317, 47, 633, 915, 952, 170], [108, 803, 372, 62, 996, 549, 696, 458], [269, 842, 415, 334]) == []
assert solution.arraysIntersection([588, 932, 150, 301], [130], [157, 529, 143, 871, 513, 644, 431, 534, 509, 707]) == []
assert solution.arraysIntersection([982, 968, 847, 95, 721, 424, 535, 887], [282, 329, 897, 705, 856, 902, 884, 91, 80, 36], [330, 241, 765, 607, 999, 622]) == []
assert solution.arraysIntersection([93, 557, 714, 229, 948, 254, 422, 386, 649, 631], [602, 526, 495, 663, 796, 691, 671, 753, 258], [971, 802, 163, 65, 747, 677, 490, 104, 25, 712]) == []
assert solution.arraysIntersection([535, 173, 959, 568, 997], [745, 394], [646, 480]) == []
assert solution.arraysIntersection([210, 699, 526, 573, 680, 816, 878, 679], [119, 774, 980, 981, 530], [663, 728, 944, 315]) == []
assert solution.arraysIntersection([452, 926, 454], [702, 629, 676, 370, 66], [41, 142, 819, 85, 525, 740, 469, 770, 546]) == []
assert solution.arraysIntersection([737, 369, 60, 385, 155], [314, 822, 845, 585, 673, 683], [815, 680, 807, 584, 76, 248, 53, 348, 877, 672]) == []
assert solution.arraysIntersection([548, 789, 628, 239, 855, 542, 505, 306, 317, 378], [278, 275, 855], [855, 328]) == [855]
assert solution.arraysIntersection([412, 151, 261, 794, 307, 143], [353, 256, 205, 908, 926, 863, 453, 966, 337], [258, 639, 85, 819]) == []
assert solution.arraysIntersection([348, 167, 298, 65, 263, 577, 109, 389], [8, 694, 936, 534, 3, 525], [300, 187, 636]) == []
assert solution.arraysIntersection([693, 326, 893, 810, 769, 851, 836, 920], [608, 504, 407, 555], [83]) == []
assert solution.arraysIntersection([55, 893, 58, 491, 981], [439, 10, 553, 545, 658, 8, 534], [264, 463, 200, 679, 51, 141]) == []
assert solution.arraysIntersection([571, 265, 875, 296, 327, 71, 693, 672], [396], [592, 931, 424, 620, 600]) == []
assert solution.arraysIntersection([770, 495], [708, 745, 252, 462, 606, 809, 396], [867, 168, 623, 880, 688, 504, 585]) == []
assert solution.arraysIntersection([10, 395, 315, 490, 527, 991, 845, 63, 797], [543, 698, 614, 576, 209], [686, 381, 927, 9, 476]) == []
assert solution.arraysIntersection([798, 112, 478, 28, 483, 469], [718, 300, 363, 421, 671, 377, 616, 865], [93, 379, 58, 608, 459, 351, 939, 366, 658, 211]) == []
assert solution.arraysIntersection([601, 467, 465, 661, 133, 509, 22, 954], [407, 204, 278, 238, 827, 391, 295, 800], [69, 723, 118, 527, 262, 963, 276]) == []
assert solution.arraysIntersection([105, 936, 89, 829, 553, 674, 55, 356], [234, 779, 818, 3, 132, 695, 967, 323, 805, 741], [690, 33, 918, 325, 618, 927, 813, 284, 859, 408]) == []