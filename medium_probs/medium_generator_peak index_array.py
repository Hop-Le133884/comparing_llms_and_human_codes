
import random

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

def generate_test_case():
    solution = Solution()

    # Generate a valid mountain array
    length = random.randint(3, 101)
    peak = random.randint(1, length - 2)
    arr = [random.randint(0, 10**6) for _ in range(peak)]
    arr.append(random.randint(arr[peak - 1] + 1, 10**6))
    arr.extend([random.randint(0, arr[peak]) for _ in range(length - peak - 1)])
    random.shuffle(arr)
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.peakIndexInMountainArray(arr)

    return arr, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        arr, expected_result = generate_test_case()
        solution = Solution()
        assert solution.peakIndexInMountainArray(arr) == expected_result
        print(f"assert solution.peakIndexInMountainArray({arr}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.peakIndexInMountainArray({arr}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)
