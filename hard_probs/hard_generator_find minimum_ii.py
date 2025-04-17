
import random

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]

def generate_test_case():
    solution = Solution()
    
    # Generate random numbers list
    nums = sorted(random.sample(range(-5000, 5001), random.randint(1, 20)))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.findMin(nums)

    return nums, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, expected_result = generate_test_case()
        solution = Solution()
        assert solution.findMin(nums) == expected_result
        print(f"assert solution.findMin({nums}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.findMin({nums}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
