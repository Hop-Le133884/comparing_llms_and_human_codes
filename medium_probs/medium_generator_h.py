
import random

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n
        while left < right:
            mid = (left + right + 1) >> 1
            if citations[n - mid] >= mid:
                left = mid
            else:
                right = mid - 1
        return left

def generate_test_case():
    solution = Solution()
    
    # Generate random citations list
    citations = sorted(random.sample(range(1001), random.randint(1, 100)))
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.hIndex(citations)

    return citations, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        citations, expected_result = generate_test_case()
        solution = Solution()
        assert solution.hIndex(citations) == expected_result
        print(f"assert solution.hIndex({citations}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.hIndex({citations}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)
