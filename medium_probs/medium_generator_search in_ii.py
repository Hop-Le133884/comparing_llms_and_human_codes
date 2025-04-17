
import random

class Solution:
    def search(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[r]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:
                r -= 1
        return nums[l] == target

def generate_test_case():
    solution = Solution()
    
    # Generate a random length for the nums list
    n = random.randint(1, 10)
    
    # Generate a random list of numbers for nums
    nums = sorted(random.sample(range(-10000, 10001), n))
    
    # Generate a random target number
    target = random.randint(-10000, 10001)

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
        test_case_generator_results.append(f"assert solution.search({nums}, {target}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
