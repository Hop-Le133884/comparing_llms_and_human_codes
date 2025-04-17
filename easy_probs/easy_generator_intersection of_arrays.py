
import random

class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        cnt = Counter(arr1 + arr2 + arr3)
        return [x for x in arr1 if cnt[x] == 3]

def generate_test_case():
    solution = Solution()
    
    # Generate random arrays
    arr1 = random.sample(range(1, 1001), random.randint(1, 10))
    arr2 = random.sample(range(1, 1001), random.randint(1, 10))
    arr3 = random.sample(range(1, 1001), random.randint(1, 10))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.arraysIntersection(arr1, arr2, arr3)

    return arr1, arr2, arr3, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        arr1, arr2, arr3, expected_result = generate_test_case()
        solution = Solution()
        assert solution.arraysIntersection(arr1, arr2, arr3) == expected_result
        print(f"assert solution.arraysIntersection({arr1}, {arr2}, {arr3}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.arraysIntersection({arr1}, {arr2}, {arr3}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
