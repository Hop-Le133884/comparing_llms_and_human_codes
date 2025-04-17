
import random

class Solution:
    def findMin(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

def generate_test_case():
    solution = Solution()
    
    # Generate a random sorted rotated array with unique elements
    nums = random.sample(range(-5000, 5001), random.randint(1, 100))
    nums.sort()
    rotate_times = random.randint(1, len(nums))
    nums = nums[rotate_times:] + nums[:rotate_times]
    
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
        test_case_generator_results.append(f"assert solution.findMin({nums}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)
