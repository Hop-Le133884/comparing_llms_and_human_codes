
import random

class RangeFreqQueryTest:
    def __init__(self, arr):
        self.arr = arr
    
    def generate_test_case(self):
        # Generate random indices
        left = random.randint(0, len(self.arr)-1)
        right = random.randint(left, len(self.arr)-1)
        
        # Generate a random value
        value = random.randint(1, 10001)
        
        # Calculate the expected result using the provided RangeFreqQuery class
        freq_query = RangeFreqQuery(self.arr)
        expected_result = freq_query.query(left, right, value)
        
        return left, right, value, expected_result
    
    def test_generated_test_cases(self, num_tests):
        test_case_generator_results = []
        for i in range(num_tests):
            left, right, value, expected_result = self.generate_test_case()
            freq_query = RangeFreqQuery(self.arr)
            assert freq_query.query(left, right, value) == expected_result
            print(f"assert freq_query.query({left}, {right}, {value}) == {expected_result}")
            test_case_generator_results.append(f"assert freq_query.query({left}, {right}, {value}) == {expected_result}")
        return test_case_generator_results

if __name__ == "__main__":
    arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]  # You can change this to generate test cases for different arrays
    num_tests = 100  # You can change this to generate more test cases
    range_freq_query_test = RangeFreqQueryTest(arr)
    test_case_generator_results = range_freq_query_test.test_generated_test_cases(num_tests)
