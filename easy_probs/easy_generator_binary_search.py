
import random

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1


def generate_test_case():
    solution = Solution()
    
    # Generate random numbers list
    nums = sorted(random.sample(range(-10000, 10000), random.randint(1, 10001)))
    
    # Generate a random target value
    target = random.randint(-10000, 10000)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.search(nums, target)

    return nums, target, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, target, expected_result = generate_test_case()
        solution = Solution()
        assert solution.search(nums, target) == expected_result
        print(f"assert solution.search({nums}, {target}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.search({nums}, {target}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
