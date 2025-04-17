
import random
import bisect

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(x):
            if x == 0:
                return 0
            return x // 5 + f(x // 5)

        def g(k):
            return bisect.bisect_left(range(5 * k), k, key=f)

        return g(k + 1) - g(k)

def generate_test_case():
    solution = Solution()

    # Generate a random k value
    k = random.randint(0, 101)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.preimageSizeFZF(k)

    return k, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.preimageSizeFZF(k) == expected_result
        print(f"assert solution.preimageSizeFZF({k}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.preimageSizeFZF({k}) == {expected_result}") 
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)
