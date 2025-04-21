# hard_query.py

from collections import Counter

class LLM_Solution:
    def __init__(self, arr):
        self.arr = arr
    
    def query(self, left, right, threshold):
        # Extract the subarray within the range [left, right]
        subarray = self.arr[left:right + 1]
        
        # Count the occurrences of each element in the subarray
        count = Counter(subarray)
        
        # Find the majority element by checking the count
        for key, value in count.items():
            if value >= threshold:
                return key
        return -1
