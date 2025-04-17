
import random

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(a, b, c)
        l, r = 1, 2 * 10**9
        while l < r:
            mid = (l + r) >> 1
            if (
                mid // a
                + mid // b
                + mid // c
                - mid // ab
                - mid // bc
                - mid // ac
                + mid // abc
                >= n
            ):
                r = mid
            else:
                l = mid + 1
        return l

def generate_test_case():
    solution = Solution()
    
    # Generate random values for n, a, b, c
    n = random.randint(1, 101)
    a = random.randint(1, 1000000000)
    b = random.randint(1, 1000000000)
    c = random.randint(1, 1000000000)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.nthUglyNumber(n, a, b, c)

    return n, a, b, c, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        n, a, b, c, expected_result = generate_test_case()
        solution = Solution()
        assert solution.nthUglyNumber(n, a, b, c) == expected_result
        print(f"assert solution.nthUglyNumber({n}, {a}, {b}, {c}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.nthUglyNumber({n}, {a}, {b}, {c}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)
