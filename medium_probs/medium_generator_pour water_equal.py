
import random

class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        def check(v):
            a = b = 0
            for x in buckets:
                if x >= v:
                    a += x - v
                else:
                    b += (v - x) * 100 / (100 - loss)
            return a >= b

        l, r = 0, max(buckets)
        while r - l > 1e-5:
            mid = (l + r) / 2
            if check(mid):
                l = mid
            else:
                r = mid
        return l

def generate_test_case():
    solution = Solution()
    
    # Generate random buckets list
    buckets = random.sample(range(1, 101), random.randint(1, 10))
    
    # Generate a random loss percentage
    loss = random.randint(0, 99)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.equalizeWater(buckets, loss)

    return buckets, loss, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        buckets, loss, expected_result = generate_test_case()
        solution = Solution()
        assert solution.equalizeWater(buckets, loss) == expected_result
        print(f"assert solution.equalizeWater({buckets}, {loss}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.equalizeWater({buckets}, {loss}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
