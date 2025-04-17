
import random
from math import gcd
from itertools import accumulate
from typing import List

class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        f = []
        ans = 0
        for i, v in enumerate(nums):
            g = []
            for j, x in f:
                y = gcd(x, v)
                if not g or g[-1][1] != y:
                    g.append((j, y))
            f = g
            f.append((i, v))
            for j, x in f:
                if i - j + 1 >= k:
                    ans = max(ans, (s[i + 1] - s[j]) * x)
        return ans


def generate_test_case():
    solution = Solution()
    
    # Generate random numbers list
    nums = random.sample(range(1, 10**6 + 1), random.randint(2, 10))
    
    # Generate a random value for k
    k = random.randint(1, len(nums))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.maxGcdSum(nums, k)

    return nums, k, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.maxGcdSum(nums, k) == expected_result
        print(f"assert solution.maxGcdSum({nums}, {k}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.maxGcdSum({nums}, {k}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
