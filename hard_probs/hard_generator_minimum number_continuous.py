
import random
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans, j = n, 0
        for i, v in enumerate(nums):
            while j < len(nums) and nums[j] - v <= n - 1:
                j += 1
            ans = min(ans, n - (j - i))
        return ans

def generate_test_case():
    solution = Solution()
    
    # Generate random numbers list
    nums = random.sample(range(1, 101), random.randint(2, 10))
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.minOperations(nums)

    return nums, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, expected_result = generate_test_case()
        solution = Solution()
        assert solution.minOperations(nums) == expected_result
        print(f"assert solution.minOperations({nums}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.minOperations({nums}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
