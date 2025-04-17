
def generate_test_case():
    solution = Solution()
    
    # Generate a random neededApples value
    neededApples = random.randint(1, 10**15)
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.minimumPerimeter(neededApples)

    return neededApples, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        neededApples, expected_result = generate_test_case()
        solution = Solution()
        assert solution.minimumPerimeter(neededApples) == expected_result
        print(f"assert solution.minimumPerimeter({neededApples}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.minimumPerimeter({neededApples}) == {expected_result}") 
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  
    test_case_generator_results = test_generated_test_cases(num_tests)
