
import random
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) >> 1
            if ord(letters[mid]) > ord(target):
                right = mid
            else:
                left = mid + 1
        return letters[left % len(letters)]

def generate_test_case():
    solution = Solution()
    
    # Generate random letters list
    letters = [chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(2, 10))]
    letters.sort()

    # Generate a random target character
    target = chr(random.randint(ord('a'), ord('z')))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.nextGreatestLetter(letters, target)

    return letters, target, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        letters, target, expected_result = generate_test_case()
        solution = Solution()
        assert solution.nextGreatestLetter(letters, target) == expected_result
        print(f"assert solution.nextGreatestLetter({letters}, '{target}') == '{expected_result}'")
        test_case_generator_results.append(f"assert solution.nextGreatestLetter({letters}, '{target}') == '{expected_result}'") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
