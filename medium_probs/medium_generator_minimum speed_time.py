
import random

class Solution:
    def minSpeedOnTime(self, dist, hour):
        def check(speed):
            res = 0
            for i, d in enumerate(dist):
                res += (d / speed) if i == len(dist) - 1 else math.ceil(d / speed)
            return res <= hour

        r = 10**7 + 1
        ans = bisect_left(range(1, r), True, key=check) + 1
        return -1 if ans == r else ans


def generate_test_case():
    solution = Solution()

    # Generate random numbers list
    dist = random.sample(range(1, 101), random.randint(2, 10))

    # Generate a random hour
    hour = round(random.uniform(1, 100), 2)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.minSpeedOnTime(dist, hour)

    return dist, hour, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        dist, hour, expected_result = generate_test_case()
        solution = Solution()
        assert solution.minSpeedOnTime(dist, hour) == expected_result
        print(f"assert solution.minSpeedOnTime({dist}, {hour}) == {expected_result}")
        test_case_generator_results.append(
            f"assert solution.minSpeedOnTime({dist}, {hour}) == {expected_result}"
        )  # You can find that we construct the test case in the same format as the example
    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
