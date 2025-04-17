
import random
from collections import Counter

class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = Counter()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.counter[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        return sum([v for t, v in self.counter.items() if t + 300 > timestamp])


def generate_test_case():
    # Initialize HitCounter object
    hit_counter = HitCounter()

    # Generate random number of hits
    num_hits = random.randint(1, 20)
    hits = [random.randint(1, 2000) for _ in range(num_hits)]

    # Store the timestamps and expected results for getHits() calls
    timestamps = []
    expected_results = []

    # Hit the counter at each timestamp
    for hit in hits:
        hit_counter.hit(hit)

        # Generate random timestamp for getHits() call
        timestamp = random.randint(1, 2000)
        timestamps.append(timestamp)

        # Calculate the expected result using the hit_counter object
        expected_result = hit_counter.getHits(timestamp)
        expected_results.append(expected_result)

    return hits, timestamps, expected_results


def test_generated_test_cases(num_tests):
    random.seed(42) # Set seed for reproducibility
    test_case_generator_results = []

    for _ in range(num_tests):
        hits, timestamps, expected_results = generate_test_case()

        # Generate the assert statement for each test case
        for i in range(len(hits)):
            test_case_generator_results.append(f"assert solution.hit({hits[i]}) == None")
            test_case_generator_results.append(f"assert solution.getHits({timestamps[i]}) == {expected_results[i]}")

    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
