
import random

# Define the Solution class
class Solution:
    def kIncreasing(self, arr, k):
        def lis(arr):
            t = []
            for x in arr:
                idx = bisect_right(t, x)
                if idx == len(t):
                    t.append(x)
                else:
                    t[idx] = x
            return len(arr) - len(t)

        return sum(lis(arr[i::k]) for i in range(k))


def generate_test_case():
    solution = Solution()
    
    # Generate a random array of positive integers
    arr = [random.randint(1, 100) for _ in range(random.randint(1, 10))]

    # Generate a random k value
    k = random.randint(1, len(arr))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.kIncreasing(arr, k)

    return arr, k, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for _ in range(num_tests):
        arr, k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.kIncreasing(arr, k) == expected_result
        test_case_generator_results.append(f"assert solution.kIncreasing({arr}, {k}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)
