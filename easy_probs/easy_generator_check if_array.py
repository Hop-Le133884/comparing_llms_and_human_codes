
import random

class Solution:
    def isMajorityElement(self, nums, target):
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return right - left > len(nums) // 2

def generate_test_case():
    solution = Solution()
    
    # Generate a nums list
    nums = [random.randint(1, 10**9) for _ in range(random.randint(1, 1001))]
    
    # Generate a target
    target = random.randint(1, 10**9)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.isMajorityElement(nums, target)

    return nums, target, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, target, expected_result = generate_test_case()
        solution = Solution()
        assert solution.isMajorityElement(nums, target) == expected_result
        print(f"assert solution.isMajorityElement({nums}, {target}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.isMajorityElement({nums}, {target}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
