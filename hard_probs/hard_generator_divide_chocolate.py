
import random

class Solution:
    def maximizeSweetness(self, sweetness, k):
        def check(x):
            s = cnt = 0
            for v in sweetness:
                s += v
                if s >= x:
                    s = 0
                    cnt += 1
            return cnt > k

        l, r = 0, sum(sweetness)
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l

def generate_test_case():
    solution = Solution()
    
    # Generate random sweetness list
    sweetness = random.sample(range(1, 101), random.randint(1, 10))

    # Generate a random k value
    k = random.randint(0, len(sweetness) - 1)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.maximizeSweetness(sweetness, k)

    return sweetness, k, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        sweetness, k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.maximizeSweetness(sweetness, k) == expected_result
        print(f"assert solution.maximizeSweetness({sweetness}, {k}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.maximizeSweetness({sweetness}, {k}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)
