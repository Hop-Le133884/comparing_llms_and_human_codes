
import random
from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(k):
            i = j = 0
            ids = set(removable[:k])
            while i < m and j < n:
                if i not in ids and s[i] == p[j]:
                    j += 1
                i += 1
            return j == n

        m, n = len(s), len(p)
        left, right = 0, len(removable)
        while left < right:
            mid = (left + right + 1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left

def generate_test_case():
    solution = Solution()

    # Generate random strings
    s_len = random.randint(2, 10)
    s = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=s_len))
    
    p_len = random.randint(1, s_len)
    p = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=p_len))
    
    # Generate random removable indices
    max_removable = min(len(s), s_len - p_len)
    removable = random.sample(range(len(s)), random.randint(0, max_removable))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.maximumRemovals(s, p, removable)

    return s, p, removable, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        s, p, removable, expected_result = generate_test_case()
        solution = Solution()
        assert solution.maximumRemovals(s, p, removable) == expected_result
        test_case_generator_results.append(f"assert solution.maximumRemovals('{s}', '{p}', {removable}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
