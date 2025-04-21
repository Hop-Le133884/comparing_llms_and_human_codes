# hard_query.py

from typing import List

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.indices = {}
        for i, num in enumerate(arr):
            if num not in self.indices:
                self.indices[num] = []
            self.indices[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(10):  # Randomized check
            idx = left + (right - left) // 2
            candidate = self.arr[idx]
            
            occurrences = self._count_occurrences(candidate, left, right)
            if occurrences >= threshold:
                return candidate
        return -1

    def _count_occurrences(self, num: int, left: int, right: int) -> int:
        if num not in self.indices:
            return 0
        
        left_idx = self._binary_search_left(self.indices[num], left)
        right_idx = self._binary_search_right(self.indices[num], right)
        return right_idx - left_idx + 1

    def _binary_search_left(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def _binary_search_right(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
class LLM_Solution:
    def query(self, arr: List[int], left: int, right: int, threshold: int) -> int:
        mc = MajorityChecker(arr)
        return mc.query(left, right, threshold)