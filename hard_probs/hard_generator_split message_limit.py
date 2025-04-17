
import random

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        sa = 0
        for k in range(1, n + 1):
            sa += len(str(k))
            sb = len(str(k)) * k
            sc = 3 * k
            if limit * k - (sa + sb + sc) >= n:
                ans = []
                i = 0
                for j in range(1, k + 1):
                    tail = f'<{j}/{k}>'
                    t = message[i : i + limit - len(tail)] + tail
                    ans.append(t)
                    i += limit - len(tail)
                return ans
        return []

def generate_test_case():
    solution = Solution()

    # Generate a random message
    message = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz ') for _ in range(random.randint(1, 30)))

    # Generate a random limit
    limit = random.randint(1, 30)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.splitMessage(message, limit)

    return message, limit, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        message, limit, expected_result = generate_test_case()
        solution = Solution()
        assert solution.splitMessage(message, limit) == expected_result
        if len(expected_result) != 0:
            print(f"assert solution.splitMessage('{message}', {limit}) == {expected_result}")
            test_case_generator_results.append(f"assert solution.splitMessage('{message}', {limit}) == {expected_result}") 
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
    print(test_case_generator_results)
