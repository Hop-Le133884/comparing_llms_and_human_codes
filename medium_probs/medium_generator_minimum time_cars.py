
import random
from math import sqrt
from bisect import bisect_left

class Solution:
    def repairCars(self, ranks, cars):
        def check(t):
            return sum(int(sqrt(t // r)) for r in ranks) >= cars

        return bisect_left(range(ranks[0] * cars * cars), True, key=check)


def generate_test_case():
    solution = Solution()
    
    # Generate random ranks list
    ranks = random.sample(range(1, 101), random.randint(2, 10))
    
    # Generate a random number of cars
    cars = random.randint(1, 10**6)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.repairCars(ranks, cars)

    return ranks, cars, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        ranks, cars, expected_result = generate_test_case()
        solution = Solution()
        assert solution.repairCars(ranks, cars) == expected_result
        print(f"assert solution.repairCars({ranks}, {cars}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.repairCars({ranks}, {cars}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
