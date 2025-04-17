
import random
from itertools import islice

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def pairwise(iterable):
            a, b = tee(iterable)
            next(b, None)
            return zip(a, b)

        def check(x):
            return sum(int((b - a) / x) for a, b in pairwise(stations)) <= k

        left, right = 0, 1e8
        while right - left > 1e-6:
            mid = (left + right) / 2
            if check(mid):
                right = mid
            else:
                left = mid
        return left


def generate_test_case():
    solution = Solution()

    # Generate an integer array
    stations = sorted(random.sample(range(1, 101), random.randint(10, 20)))

    # Generate an integer k
    k = random.randint(1, 100)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.minmaxGasDist(stations, k)

    return stations, k, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        stations, k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.minmaxGasDist(stations, k) == expected_result
        print(f"assert solution.minmaxGasDist({stations}, {k}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.minmaxGasDist({stations}, {k}) == {expected_result}")
    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
