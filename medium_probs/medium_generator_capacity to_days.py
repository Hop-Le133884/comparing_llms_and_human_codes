
import random
from bisect import bisect_left

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mx):
            ws, cnt = 0, 1
            for w in weights:
                ws += w
                if ws > mx:
                    cnt += 1
                    ws = w
            return cnt <= days

        left, right = max(weights), sum(weights) + 1
        return left + bisect_left(range(left, right), True, key=check)


def generate_test_case():
    solution = Solution()

    # Generate random weights list
    weights = random.choices(range(1, 501), k=random.randint(1, 10))

    # Generate random number of days
    days = random.randint(1, len(weights))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.shipWithinDays(weights, days)

    return weights, days, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        weights, days, expected_result = generate_test_case()
        solution = Solution()
        assert solution.shipWithinDays(weights, days) == expected_result
        print(f"assert solution.shipWithinDays({weights}, {days}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.shipWithinDays({weights}, {days}) == {expected_result}")
    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
