
import random

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        s = k = 0
        while 1:
            if s >= target and (s - target) % 2 == 0:
                return k
            k += 1
            s += k

def generate_test_case():
    solution = Solution()
    
    # Generate a random target
    target = random.randint(-10**9, 10**9)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.reachNumber(target)

    return target, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        target, expected_result = generate_test_case()
        solution = Solution()
        assert solution.reachNumber(target) == expected_result
        print(f"assert solution.reachNumber({target}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.reachNumber({target}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
