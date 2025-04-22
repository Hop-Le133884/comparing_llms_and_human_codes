
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
    def minmaxGasDist(self, stations, k):
        left, right = 0, stations[-1] - stations[0]
        while right - left > 1e-6:
            mid = (left + right) / 2
            count = 0
            for i in range(len(stations) - 1):
                count += int((stations[i+1] - stations[i]) / mid)
            if count <= k:
                right = mid
            else:
                left = mid
        return left

solution=Solution()
assert solution.minmaxGasDist([2, 16, 21, 23, 28, 30, 37, 42, 44, 50, 74, 82, 83, 84, 87, 92], 73) == 1.0769227287710237
assert solution.minmaxGasDist([6, 16, 29, 31, 35, 48, 49, 52, 54, 56, 71, 78, 81, 87, 92, 97, 100], 5) == 6.999999868639861
assert solution.minmaxGasDist([4, 19, 23, 30, 40, 46, 57, 60, 65, 79, 82, 87, 90], 95) == 0.8333330470122746
assert solution.minmaxGasDist([2, 13, 21, 29, 34, 39, 41, 45, 50, 64, 67, 81, 85, 94, 99], 73) == 1.249999570518412
assert solution.minmaxGasDist([3, 9, 11, 20, 22, 23, 29, 43, 44, 46, 70, 71, 73, 84, 89, 97, 99], 100) == 0.899999719194966
assert solution.minmaxGasDist([5, 18, 22, 27, 38, 39, 47, 49, 59, 67, 68, 71, 76, 77, 79, 82, 88, 89, 93], 9) == 4.999999703159119
assert solution.minmaxGasDist([5, 6, 15, 20, 23, 31, 35, 43, 44, 79, 99], 87) == 0.9999993721976352
assert solution.minmaxGasDist([1, 6, 8, 16, 29, 31, 34, 37, 38, 49, 51, 54, 57, 67, 69, 72, 74, 81, 94, 98], 61) == 1.3999994052937836
assert solution.minmaxGasDist([11, 21, 23, 44, 45, 54, 58, 66, 68, 77, 79, 81, 82, 88, 89, 93, 95, 96, 98, 99], 100) == 0.8076916913068999
assert solution.minmaxGasDist([2, 10, 13, 15, 22, 26, 37, 51, 53, 59, 63, 89, 98], 33) == 2.3333328158514632
assert solution.minmaxGasDist([1, 15, 20, 25, 29, 39, 44, 53, 60, 88], 98) == 0.8333330470122746
assert solution.minmaxGasDist([10, 12, 28, 37, 43, 52, 62, 66, 74, 75], 21) == 2.4999998515795596
assert solution.minmaxGasDist([1, 15, 16, 35, 61, 63, 79, 94, 96, 100], 74) == 1.249999570518412
assert solution.minmaxGasDist([16, 31, 33, 36, 56, 60, 61, 72, 75, 77, 83, 85, 92], 29) == 1.9999994549380062
assert solution.minmaxGasDist([5, 8, 14, 18, 19, 24, 31, 33, 37, 44, 55, 64, 67, 69, 75, 85, 89, 90, 94, 100], 92) == 0.9999993721976352
assert solution.minmaxGasDist([2, 5, 8, 11, 19, 20, 30, 36, 42, 45, 57, 73, 77, 78], 60) == 1.111110492502121
assert solution.minmaxGasDist([4, 11, 27, 29, 37, 39, 41, 57, 61, 64, 65, 68, 76, 79, 82, 85, 86, 90], 83) == 0.9999993721976352
assert solution.minmaxGasDist([13, 17, 26, 27, 29, 30, 35, 41, 49, 50, 54, 61, 63, 67, 69, 72, 77, 91, 100], 71) == 0.9999993721976352
assert solution.minmaxGasDist([17, 19, 20, 22, 23, 27, 30, 31, 33, 38, 40, 46, 58, 63, 66, 74, 78, 82, 89, 97], 48) == 1.3333327331110922
assert solution.minmaxGasDist([4, 7, 20, 24, 27, 29, 37, 40, 46, 51, 53, 65, 69, 79, 84, 92, 93], 49) == 1.4999997688391886
assert solution.minmaxGasDist([4, 7, 11, 25, 28, 30, 33, 40, 42, 46, 48, 49, 57, 59, 73, 87, 90], 69) == 1.0769227287710237
assert solution.minmaxGasDist([6, 7, 9, 25, 36, 59, 61, 70, 71, 74, 82, 84], 64) == 1.095237678327976
assert solution.minmaxGasDist([5, 12, 20, 24, 25, 29, 36, 41, 44, 56, 58, 87, 95, 97], 52) == 1.5999994218418578
assert solution.minmaxGasDist([2, 8, 13, 29, 31, 32, 34, 49, 51, 81, 84, 85, 95], 83) == 0.9999993721976352
assert solution.minmaxGasDist([1, 16, 17, 18, 23, 32, 34, 61, 70, 71, 74, 78, 80], 67) == 0.9999993721976352
assert solution.minmaxGasDist([19, 23, 24, 36, 40, 45, 47, 52, 59, 64, 77, 91, 92, 96, 98], 74) == 0.9999993721976352
assert solution.minmaxGasDist([6, 18, 20, 23, 25, 34, 50, 51, 70, 80, 88], 38) == 1.9999994549380062
assert solution.minmaxGasDist([5, 10, 15, 19, 33, 43, 44, 59, 73, 74, 75], 63) == 0.9999993721976352
assert solution.minmaxGasDist([4, 13, 18, 19, 30, 49, 50, 53, 60, 61, 72, 82, 85, 86, 92, 93], 46) == 1.583332931431869
assert solution.minmaxGasDist([2, 3, 29, 30, 35, 53, 56, 75, 79, 84, 89], 76) == 1.03999937550725
assert solution.minmaxGasDist([5, 12, 25, 27, 28, 37, 43, 46, 57, 59, 72, 78, 83], 76) == 0.9999993721976352
assert solution.minmaxGasDist([7, 8, 10, 15, 18, 26, 30, 32, 50, 56, 57, 58, 59, 66, 67, 69, 75, 76, 78], 72) == 0.899999719194966
assert solution.minmaxGasDist([2, 16, 17, 27, 28, 29, 43, 51, 61, 63, 74, 75, 81, 85, 87, 94, 95, 96, 97], 38) == 1.9999994549380062
assert solution.minmaxGasDist([12, 13, 14, 22, 23, 24, 26, 35, 43, 48, 50, 55, 62, 78, 80, 84, 85, 87, 89, 97], 66) == 0.9999993721976352
assert solution.minmaxGasDist([12, 17, 24, 34, 38, 43, 55, 60, 62, 67, 83, 88, 92, 93, 96, 98, 100], 19) == 3.1999995542264514
assert solution.minmaxGasDist([3, 6, 13, 17, 21, 33, 35, 37, 53, 67, 71, 78, 83, 100], 3) == 11.99999957179898
assert solution.minmaxGasDist([4, 14, 19, 20, 26, 44, 49, 55, 60, 67, 68, 73, 76, 81, 89, 95], 27) == 2.4999998515795596
assert solution.minmaxGasDist([4, 14, 24, 34, 35, 40, 45, 50, 65, 67, 72, 88, 94], 23) == 2.9999995376783772
assert solution.minmaxGasDist([2, 19, 33, 40, 48, 74, 86, 87, 94, 96], 89) == 0.9999993721976352
assert solution.minmaxGasDist([20, 21, 24, 30, 33, 46, 49, 62, 78, 83, 84, 91, 93, 98], 35) == 1.8571427062852308
assert solution.minmaxGasDist([1, 2, 15, 21, 27, 29, 30, 32, 46, 61, 63, 68, 81, 86, 89, 91], 47) == 1.6666660940245492
assert solution.minmaxGasDist([13, 17, 19, 21, 46, 54, 60, 78, 86, 96], 49) == 1.5624998184193828
assert solution.minmaxGasDist([4, 16, 17, 21, 22, 35, 41, 43, 49, 58, 60, 63, 65, 69, 74, 75, 96], 55) == 1.4999997688391886
assert solution.minmaxGasDist([2, 7, 8, 9, 11, 13, 14, 16, 31, 37, 51, 58, 62, 73, 77, 93, 96, 98, 100], 43) == 1.9999994549380062
assert solution.minmaxGasDist([3, 4, 6, 14, 16, 17, 20, 23, 26, 27, 28, 33, 34, 41, 54, 64, 66, 68, 73, 92], 86) == 0.9999993721976352
assert solution.minmaxGasDist([7, 11, 17, 20, 27, 36, 38, 39, 46, 49, 67, 72, 74, 75, 76, 97, 100], 95) == 0.9130431521953142
assert solution.minmaxGasDist([10, 26, 38, 41, 44, 45, 46, 58, 59, 69, 71, 73, 88, 92, 96], 67) == 1.111110492502121
assert solution.minmaxGasDist([1, 9, 25, 31, 34, 36, 47, 63, 65, 74, 78, 79, 80, 83, 86, 89, 100], 23) == 2.9999995376783772
assert solution.minmaxGasDist([12, 26, 31, 35, 37, 42, 44, 45, 48, 50, 54, 58, 60, 62, 67, 70, 75, 76, 84, 85], 42) == 1.3333327331110922
assert solution.minmaxGasDist([5, 6, 13, 18, 20, 21, 29, 30, 34, 36, 40, 43, 69, 73, 78, 87, 97], 95) == 0.899999719194966
assert solution.minmaxGasDist([10, 16, 26, 27, 50, 61, 66, 76, 80, 86, 87, 100], 92) == 0.9199993655784056
assert solution.minmaxGasDist([20, 31, 37, 39, 51, 64, 65, 73, 83, 90, 94], 43) == 1.4999997688391886
assert solution.minmaxGasDist([4, 10, 15, 23, 28, 38, 51, 54, 56, 58, 68, 96], 61) == 1.3999994052937836
assert solution.minmaxGasDist([7, 20, 22, 30, 35, 37, 40, 41, 43, 44, 58, 61, 65, 68, 69, 80, 84], 61) == 0.9999993721976352
assert solution.minmaxGasDist([3, 20, 23, 24, 27, 42, 43, 48, 50, 56, 61, 63, 64, 68, 75, 82, 91, 93], 88) == 0.9999993721976352
assert solution.minmaxGasDist([2, 3, 8, 18, 23, 31, 38, 48, 51, 55, 57, 61, 82, 84], 49) == 1.428571039241433
assert solution.minmaxGasDist([3, 6, 14, 19, 33, 37, 46, 51, 55, 59, 66, 72, 75, 76, 91, 94, 98], 53) == 1.4999997688391886
assert solution.minmaxGasDist([19, 26, 35, 44, 45, 46, 49, 50, 51, 57, 62, 64, 71, 74, 84], 72) == 0.8333330470122746
assert solution.minmaxGasDist([3, 7, 12, 33, 36, 45, 51, 52, 59, 62, 63, 68, 69, 71, 82, 90], 70) == 1.0999997357430402
assert solution.minmaxGasDist([3, 6, 29, 30, 37, 47, 49, 52, 73, 77, 78, 79, 81, 84, 89, 96], 44) == 1.7499999671599653
assert solution.minmaxGasDist([5, 12, 15, 21, 29, 46, 48, 50, 53, 55, 72, 74, 84, 86, 87, 89], 50) == 1.4999997688391886
assert solution.minmaxGasDist([8, 18, 20, 36, 38, 54, 58, 74, 83, 94, 95], 19) == 3.6666662595052912
assert solution.minmaxGasDist([2, 4, 6, 13, 19, 20, 21, 27, 42, 43, 49, 50, 53, 79, 81, 87, 88, 95, 97], 76) == 1.03999937550725
assert solution.minmaxGasDist([3, 5, 14, 25, 29, 43, 65, 72, 81, 82, 84, 88, 90, 99], 43) == 1.9999994549380062
assert solution.minmaxGasDist([1, 9, 11, 16, 17, 18, 42, 45, 49, 54, 68, 77, 83, 85, 89, 92, 98], 100) == 0.899999719194966
assert solution.minmaxGasDist([1, 11, 12, 16, 30, 40, 47, 61, 66, 76, 93, 99], 48) == 1.7499999671599653
assert solution.minmaxGasDist([5, 14, 16, 27, 44, 45, 46, 48, 49, 51, 60, 62, 65, 66, 73, 75, 79, 94, 100], 89) == 0.9999993721976352
assert solution.minmaxGasDist([1, 10, 12, 20, 23, 24, 31, 33, 35, 39, 41, 44, 63, 66, 73, 80, 98], 43) == 1.9999994549380062
assert solution.minmaxGasDist([9, 11, 23, 35, 37, 39, 50, 54, 57, 64, 93, 95, 100], 96) == 0.9062496530987119
assert solution.minmaxGasDist([10, 13, 14, 28, 32, 40, 52, 64, 65, 74, 76, 85, 90, 93, 95], 51) == 1.4999997688391886
assert solution.minmaxGasDist([1, 2, 10, 14, 16, 18, 27, 30, 34, 36, 40, 53, 61, 71, 72, 91, 93], 16) == 3.9999996204187482
assert solution.minmaxGasDist([4, 15, 32, 39, 46, 59, 70, 73, 87, 92, 99, 100], 71) == 1.2222216128066066
assert solution.minmaxGasDist([8, 19, 21, 30, 40, 43, 52, 54, 69, 71, 72, 75, 76, 82, 86, 90, 98], 96) == 0.8823526798096282
assert solution.minmaxGasDist([33, 38, 47, 53, 54, 57, 58, 64, 67, 71, 80, 91], 74) == 0.7499998844195943
assert solution.minmaxGasDist([5, 7, 22, 24, 26, 27, 37, 41, 42, 43, 69, 70, 71, 91], 61) == 1.249999570518412
assert solution.minmaxGasDist([9, 23, 28, 33, 47, 48, 49, 50, 63, 64, 66, 68, 70, 73, 89, 90, 91, 92, 99], 20) == 3.1999995542264514
assert solution.minmaxGasDist([8, 14, 16, 27, 41, 45, 61, 63, 75, 76, 81], 94) == 0.7333326834668696
assert solution.minmaxGasDist([9, 12, 16, 17, 22, 43, 46, 50, 52, 57, 72, 76, 77, 85, 86, 92, 97], 75) == 0.9999993721976352
assert solution.minmaxGasDist([5, 8, 20, 23, 28, 30, 37, 47, 54, 61, 71, 94], 66) == 1.249999570518412
assert solution.minmaxGasDist([2, 10, 17, 21, 25, 27, 30, 33, 35, 37, 38, 44, 49, 55, 72, 74, 94, 99], 13) == 4.249999818739525
assert solution.minmaxGasDist([5, 15, 35, 42, 54, 60, 63, 79, 87, 91, 92], 42) == 1.8181815164552972
assert solution.minmaxGasDist([3, 7, 15, 16, 21, 28, 31, 39, 45, 53, 54, 59, 62, 64, 66, 85, 88, 99], 17) == 3.799999603870674
assert solution.minmaxGasDist([1, 2, 4, 18, 20, 32, 34, 48, 55, 61, 66, 71, 91, 96, 97], 62) == 1.3999994052937836
assert solution.minmaxGasDist([3, 21, 22, 37, 69, 70, 81, 85, 86, 88], 72) == 1.0714281017953908
assert solution.minmaxGasDist([11, 12, 13, 43, 55, 69, 70, 71, 72, 85, 91, 93, 99], 17) == 3.9999996204187482
assert solution.minmaxGasDist([18, 21, 25, 35, 36, 40, 42, 55, 56, 62, 71, 72, 81, 87, 94, 95], 88) == 0.8124999339997885
assert solution.minmaxGasDist([8, 12, 15, 18, 21, 24, 28, 35, 64, 92, 97, 98], 76) == 1.0740734524006257
assert solution.minmaxGasDist([15, 29, 36, 46, 51, 54, 60, 70, 80, 86, 89], 77) == 0.9090904029562807
assert solution.minmaxGasDist([6, 17, 18, 35, 38, 46, 53, 55, 60, 64, 70, 74, 82, 93, 97], 50) == 1.5714284984369442
assert solution.minmaxGasDist([20, 30, 37, 39, 42, 44, 57, 67, 69, 73, 85, 92, 93], 31) == 1.9999994549380062
assert solution.minmaxGasDist([9, 22, 24, 35, 38, 44, 46, 58, 66, 68, 77, 79, 90], 18) == 2.9999995376783772
assert solution.minmaxGasDist([1, 13, 36, 48, 50, 61, 67, 77, 79, 89, 92, 97, 98], 32) == 2.4999998515795596
assert solution.minmaxGasDist([6, 9, 26, 27, 37, 41, 43, 56, 64, 68, 70, 71, 73, 77, 91, 95, 97], 8) == 5.666666424986033
assert solution.minmaxGasDist([9, 10, 29, 51, 52, 60, 62, 64, 65, 72, 74, 83, 84], 57) == 1.1428568313931464
assert solution.minmaxGasDist([3, 4, 11, 12, 13, 15, 18, 26, 27, 33, 34, 41, 46, 47, 51, 63, 66, 94, 97, 99], 33) == 2.3333328158514632
assert solution.minmaxGasDist([19, 22, 25, 42, 49, 50, 68, 79, 80, 93, 97], 84) == 0.8749999835799827
assert solution.minmaxGasDist([15, 22, 24, 30, 35, 37, 39, 41, 47, 49, 50, 64, 69, 70, 77, 84, 88, 96], 40) == 1.7499999671599653
assert solution.minmaxGasDist([8, 11, 20, 31, 36, 72, 81, 88, 89, 90], 49) == 1.4999997688391886
assert solution.minmaxGasDist([2, 8, 13, 27, 29, 34, 48, 50, 54, 55, 57, 58, 60, 62, 85, 86, 90], 71) == 1.0454542120896804
assert solution.minmaxGasDist([3, 10, 39, 42, 51, 54, 56, 58, 71, 74, 75, 79, 85, 87, 95, 99], 4) == 8.999999323577867