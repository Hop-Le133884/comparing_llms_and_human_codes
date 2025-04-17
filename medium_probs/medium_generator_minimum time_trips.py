
import random

class Solution:
    def minimumTime(self, time, totalTrips):
        mx = min(time) * totalTrips
        return bisect_left(
            range(mx), totalTrips, key=lambda x: sum(x // v for v in time)
        )
        
def generate_test_case():
    solution = Solution()
    
    # Generate random numbers list
    time = [random.randint(1, 101) for _ in range(random.randint(1, 10))]
    
    # Generate a random totalTrips
    totalTrips = random.randint(1, 1001)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.minimumTime(time, totalTrips)

    return time, totalTrips, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        time, totalTrips, expected_result = generate_test_case()
        solution = Solution()
        assert solution.minimumTime(time, totalTrips) == expected_result
        print(f"assert solution.minimumTime({time}, {totalTrips}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.minimumTime({time}, {totalTrips}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
