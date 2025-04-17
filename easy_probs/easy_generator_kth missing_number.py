
from typing import List
import random

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

def generate_test_case():
    solution = Solution()
    
    # Generate a sorted list of positive integers
    arr = sorted(random.sample(range(1, 1001), random.randint(1, 10)))
    
    # Generate a random k value
    k = random.randint(1, 1001)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.findKthPositive(arr, k)

    return arr, k, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        arr, k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.findKthPositive(arr, k) == expected_result
        print(f"assert solution.findKthPositive({arr}, {k}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.findKthPositive({arr}, {k}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
