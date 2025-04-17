
import random

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def f(x):
            cnt, j = 0, -2
            for i, v in enumerate(nums):
                if v > x or i == j + 1:
                    continue
                cnt += 1
                j = i
            return cnt >= k

        return bisect_left(range(max(nums) + 1), True, key=f)


def generate_test_case():
    solution = Solution()

    # Generate random numbers list
    nums = random.sample(range(1, 101), random.randint(2, 10))

    # Generate a random k
    k = random.randint(1, len(nums) // 2 + 1)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.minCapability(nums, k)

    return nums, k, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.minCapability(nums, k) == expected_result
        print(f"assert solution.minCapability({nums}, {k}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.minCapability({nums}, {k}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
