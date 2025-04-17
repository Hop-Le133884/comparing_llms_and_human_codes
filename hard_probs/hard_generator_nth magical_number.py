
import random

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7
        c = lcm(a, b)
        r = (a + b) * n
        return bisect_left(range(r), x=n, key=lambda x: x // a + x // b - x // c) % mod

def generate_test_case():
    solution = Solution()
    
    # Generate random numbers
    n = random.randint(1, 101)
    a = random.randint(2, 1001)
    b = random.randint(2, 1001)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.nthMagicalNumber(n, a, b)

    return n, a, b, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        n, a, b, expected_result = generate_test_case()
        solution = Solution()
        assert solution.nthMagicalNumber(n, a, b) == expected_result
        print(f"assert solution.nthMagicalNumber({n}, {a}, {b}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.nthMagicalNumber({n}, {a}, {b}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
