
import random
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            # Equals to: if (mid % 2 == 0 and nums[mid] != nums[mid + 1]) or (mid % 2 == 1 and nums[mid] != nums[mid - 1]):
            if nums[mid] != nums[mid ^ 1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

def generate_test_case():
    solution = Solution()
    
    # Generate random numbers list
    nums = []
    for i in range(50):
        nums.append(i)
        nums.append(i)
    nums.append(random.randint(0, 49))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.singleNonDuplicate(nums)

    return nums, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, expected_result = generate_test_case()
        solution = Solution()
        assert solution.singleNonDuplicate(nums) == expected_result
        print(f"assert solution.singleNonDuplicate({nums}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.singleNonDuplicate({nums}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
