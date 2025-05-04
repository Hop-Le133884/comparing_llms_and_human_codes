
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
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) >> 1
            if ord(letters[mid]) > ord(target):
                right = mid
            else:
                left = mid + 1
        return letters[left % len(letters)]

solution=Solution()
assert solution.nextGreatestLetter(['a', 'p', 'p', 'v', 'y'], 'j') == 'p'
assert solution.nextGreatestLetter(['c', 'e', 'g', 'r', 'y'], 'f') == 'g'
assert solution.nextGreatestLetter(['d', 'h', 'j', 'r', 'v'], 'k') == 'r'
assert solution.nextGreatestLetter(['c', 'g', 'h', 'k', 'm', 'm', 'n', 'o', 'p', 'w'], 'e') == 'g'
assert solution.nextGreatestLetter(['c', 'd', 'd', 'm', 'q', 't', 'v'], 'w') == 'c'
assert solution.nextGreatestLetter(['b', 'h', 'j'], 'y') == 'b'
assert solution.nextGreatestLetter(['d', 'f', 'j', 'j', 'k', 'p', 's', 'u'], 'r') == 's'
assert solution.nextGreatestLetter(['k', 'n', 'r', 'r'], 'g') == 'k'
assert solution.nextGreatestLetter(['a', 'k', 'l', 'q', 's', 'w'], 'h') == 'k'
assert solution.nextGreatestLetter(['r', 'x'], 'd') == 'r'
assert solution.nextGreatestLetter(['l', 'l', 'l', 'v', 'z'], 'y') == 'z'
assert solution.nextGreatestLetter(['h', 'm', 'u', 'y'], 'a') == 'h'
assert solution.nextGreatestLetter(['i', 'n', 'p', 's', 't', 'u', 'x'], 't') == 'u'
assert solution.nextGreatestLetter(['b', 'd'], 'l') == 'b'
assert solution.nextGreatestLetter(['c', 'd'], 'i') == 'c'
assert solution.nextGreatestLetter(['a', 'q', 't', 'x'], 'x') == 'a'
assert solution.nextGreatestLetter(['a', 'h', 'j', 'm', 'x', 'y'], 'e') == 'h'
assert solution.nextGreatestLetter(['h', 'i', 'm', 'n', 'q', 'r', 'y', 'z'], 'l') == 'm'
assert solution.nextGreatestLetter(['q', 's'], 'w') == 'q'
assert solution.nextGreatestLetter(['p', 'u'], 'x') == 'p'
assert solution.nextGreatestLetter(['e', 'g', 'k', 'r', 'v'], 'f') == 'g'
assert solution.nextGreatestLetter(['e', 'f', 'h', 'k', 'p', 's', 'w', 'x'], 'k') == 'p'
assert solution.nextGreatestLetter(['f', 'u'], 'p') == 'u'
assert solution.nextGreatestLetter(['a', 'n', 'p', 'q', 'v', 'w', 'w'], 'r') == 'v'
assert solution.nextGreatestLetter(['b', 'c', 'd', 'd', 'k', 'k', 'm', 'q', 'u'], 'p') == 'q'
assert solution.nextGreatestLetter(['a', 'a', 'a', 'e', 'l', 'o', 'p', 'r', 'v'], 'w') == 'a'
assert solution.nextGreatestLetter(['e', 'h', 'o', 't', 'v'], 'g') == 'h'
assert solution.nextGreatestLetter(['c', 'f', 'g', 'j', 'j', 'l', 't', 'w', 'x', 'x'], 'p') == 't'
assert solution.nextGreatestLetter(['m', 'o', 's', 'w'], 'j') == 'm'
assert solution.nextGreatestLetter(['i', 'p', 'p', 'v', 'w', 'z'], 'i') == 'p'
assert solution.nextGreatestLetter(['d', 'd', 'f', 'h', 'h', 'k', 'm', 'p', 'u'], 'g') == 'h'
assert solution.nextGreatestLetter(['d', 'e', 'g', 'h', 'l', 'n', 'o', 't', 'u', 'y'], 'v') == 'y'
assert solution.nextGreatestLetter(['b', 'j', 'k', 'l', 'q', 'v', 'x'], 'r') == 'v'
assert solution.nextGreatestLetter(['c', 'c', 'd', 'j', 'm'], 'w') == 'c'
assert solution.nextGreatestLetter(['g', 'm', 'z'], 'g') == 'm'
assert solution.nextGreatestLetter(['a', 'b', 'd', 'd', 'k', 'm', 'n', 'o', 's', 'w'], 'r') == 's'
assert solution.nextGreatestLetter(['b', 'b', 'o', 't', 'x', 'y'], 'a') == 'b'
assert solution.nextGreatestLetter(['b', 'g', 'j', 'k', 'm', 's', 'v', 'v'], 'h') == 'j'
assert solution.nextGreatestLetter(['b', 'c', 'd', 'g', 'h', 'j', 'p', 'v', 'w', 'x'], 'd') == 'g'
assert solution.nextGreatestLetter(['f', 'o', 't', 'u', 'y', 'z'], 'x') == 'y'
assert solution.nextGreatestLetter(['e', 'f', 'i', 'i', 'l', 'n', 't', 'x'], 'i') == 'l'
assert solution.nextGreatestLetter(['b', 'c', 'j', 's', 'u'], 'm') == 's'
assert solution.nextGreatestLetter(['a', 'd', 'g', 'h', 'j', 'm', 'n', 'z'], 'w') == 'z'
assert solution.nextGreatestLetter(['d', 'i', 'p', 'p'], 'x') == 'd'
assert solution.nextGreatestLetter(['b', 'e', 'h', 'j', 'l', 'n'], 'a') == 'b'
assert solution.nextGreatestLetter(['b', 'e', 'g', 'h', 'h', 'j', 'o', 'o', 'p', 'v'], 'j') == 'o'
assert solution.nextGreatestLetter(['d', 'h', 'j', 'j', 'r', 'v', 'y'], 'd') == 'h'
assert solution.nextGreatestLetter(['b', 'g', 'h', 'u', 'y'], 'f') == 'g'
assert solution.nextGreatestLetter(['c', 'h', 'i', 'm', 'm', 'o', 's', 'v', 'z', 'z'], 'c') == 'h'
assert solution.nextGreatestLetter(['p', 'w', 'w'], 'd') == 'p'
assert solution.nextGreatestLetter(['f', 'f', 'h', 'i', 'j', 'y', 'z'], 'j') == 'y'
assert solution.nextGreatestLetter(['e', 'e', 'i', 'm', 'n', 'p', 'w', 'z'], 'n') == 'p'
assert solution.nextGreatestLetter(['b', 'g', 'h', 'm', 'n', 'w'], 'k') == 'm'
assert solution.nextGreatestLetter(['j', 'z'], 'x') == 'z'
assert solution.nextGreatestLetter(['v', 'v'], 'z') == 'v'
assert solution.nextGreatestLetter(['b', 'j', 'l', 'p', 's', 'y'], 'v') == 'y'
assert solution.nextGreatestLetter(['o', 'x'], 'j') == 'o'
assert solution.nextGreatestLetter(['b', 'b', 'e', 'h', 'p', 'q', 's', 't', 'u', 'y'], 'h') == 'p'
assert solution.nextGreatestLetter(['o', 'v', 'z'], 'l') == 'o'
assert solution.nextGreatestLetter(['u', 'z'], 'd') == 'u'
assert solution.nextGreatestLetter(['j', 'l', 'u', 'w', 'z', 'z'], 'g') == 'j'
assert solution.nextGreatestLetter(['c', 'd', 'e', 'e', 'h', 'v'], 'e') == 'h'
assert solution.nextGreatestLetter(['j', 'l', 'p', 'q', 't', 'u'], 'y') == 'j'
assert solution.nextGreatestLetter(['b', 'g', 'm', 's', 'y', 'y'], 'q') == 's'
assert solution.nextGreatestLetter(['m', 'x'], 'b') == 'm'
assert solution.nextGreatestLetter(['b', 'e', 'g', 'g', 'n', 'r', 'u', 'w'], 'c') == 'e'
assert solution.nextGreatestLetter(['a', 'l'], 'y') == 'a'
assert solution.nextGreatestLetter(['d', 'i', 'n', 'o', 'p', 'v'], 'w') == 'd'
assert solution.nextGreatestLetter(['e', 'i', 'o', 'z'], 'g') == 'i'
assert solution.nextGreatestLetter(['b', 'd', 'h', 'h', 'j', 'k', 'n', 't', 'y'], 'u') == 'y'
assert solution.nextGreatestLetter(['a', 'b', 'o', 'q', 's', 'u', 'w'], 't') == 'u'
assert solution.nextGreatestLetter(['f', 'j', 'q', 's', 'v'], 'e') == 'f'
assert solution.nextGreatestLetter(['a', 'c', 'd', 'h', 'i', 'k', 'o'], 't') == 'a'
assert solution.nextGreatestLetter(['e', 'j', 'p', 'r', 't', 'v'], 'l') == 'p'
assert solution.nextGreatestLetter(['a', 'd', 'f', 'o', 's'], 'm') == 'o'
assert solution.nextGreatestLetter(['k', 's'], 'o') == 's'
assert solution.nextGreatestLetter(['b', 't', 't', 'x'], 'w') == 'x'
assert solution.nextGreatestLetter(['t', 'u'], 's') == 't'
assert solution.nextGreatestLetter(['a', 'b', 'c', 'd', 'l', 't'], 'd') == 'l'
assert solution.nextGreatestLetter(['b', 'h', 'x', 'z'], 'f') == 'h'
assert solution.nextGreatestLetter(['d', 'e', 'v', 'x'], 'n') == 'v'
assert solution.nextGreatestLetter(['a', 'd', 'k', 'l', 'o', 'p', 'q', 'v'], 'b') == 'd'
assert solution.nextGreatestLetter(['a', 'j', 'n', 's', 'u', 'w'], 'b') == 'j'
assert solution.nextGreatestLetter(['f', 'r', 'z'], 'k') == 'r'
assert solution.nextGreatestLetter(['b', 'd', 'g', 'i', 'w', 'y'], 'g') == 'i'
assert solution.nextGreatestLetter(['e', 'h', 'n', 'o'], 'i') == 'n'
assert solution.nextGreatestLetter(['b', 'e', 'k', 'k'], 'o') == 'b'
assert solution.nextGreatestLetter(['h', 'm'], 'q') == 'h'
assert solution.nextGreatestLetter(['d', 'm', 'n', 'r', 's', 'v', 'w'], 'a') == 'd'
assert solution.nextGreatestLetter(['c', 'f', 'i', 'k', 'o', 'o', 'p', 'p', 'u', 'u'], 'o') == 'p'
assert solution.nextGreatestLetter(['e', 'j', 'm', 'o', 'x', 'z'], 'g') == 'j'
assert solution.nextGreatestLetter(['b', 'c', 'e', 'f', 'n', 'p', 'r', 'u', 'v'], 'x') == 'b'
assert solution.nextGreatestLetter(['d', 'n', 'w'], 'g') == 'n'
assert solution.nextGreatestLetter(['b', 't', 'y'], 'q') == 't'
assert solution.nextGreatestLetter(['f', 'g', 's', 'y'], 'k') == 's'
assert solution.nextGreatestLetter(['a', 'm', 'o', 'u', 'x'], 'i') == 'm'
assert solution.nextGreatestLetter(['a', 'a', 'f', 'i', 'k', 'p', 't', 't', 'z'], 'z') == 'a'
assert solution.nextGreatestLetter(['o', 'u', 'w', 'y'], 'x') == 'y'
assert solution.nextGreatestLetter(['g', 'u'], 'o') == 'u'
assert solution.nextGreatestLetter(['h', 'm', 'r', 'x', 'y', 'z', 'z'], 'p') == 'r'