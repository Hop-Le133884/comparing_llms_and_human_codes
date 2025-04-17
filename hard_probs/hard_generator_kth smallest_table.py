
import random

class Solution:
    def findKthNumber(self, m, n, k):
        left, right = 1, m * n
        while left < right:
            mid = (left + right) >> 1
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(mid // i, n)
            if cnt >= k:
                right = mid
            else:
                left = mid + 1
        return left

def generate_test_case():
    solution = Solution()
    
    # Generate random values for m, n, and k
    m = random.randint(1, 1001)
    n = random.randint(1, 1001)
    k = random.randint(1, m * n)
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.findKthNumber(m, n, k)

    return m, n, k, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        m, n, k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.findKthNumber(m, n, k) == expected_result
        print(f"assert solution.findKthNumber({m}, {n}, {k}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.findKthNumber({m}, {n}, {k}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)
