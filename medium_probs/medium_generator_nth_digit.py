
def generate_test_case():
    solution = Solution()
    
    # Generate a random n value
    n = random.randint(1, 100)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.findNthDigit(n)

    return n, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        n, expected_result = generate_test_case()
        solution = Solution()
        assert solution.findNthDigit(n) == expected_result
        print(f"assert solution.findNthDigit({n}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.findNthDigit({n}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
