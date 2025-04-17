
import random

class Solution:
    def generate_test_case(self):
        piles = random.choices(range(1, int(1e9)), k=random.randint(1, 10))
        h = random.randint(len(piles), int(1e9))
        expected_result = self.minEatingSpeed(piles, h)
        return piles, h, expected_result

    def test_generated_test_cases(self, num_tests):
        test_case_generator_results = []
        for _ in range(num_tests):
            piles, h, expected_result = self.generate_test_case()
            assert self.minEatingSpeed(piles, h) == expected_result
            test_case_generator_results.append(f"assert self.minEatingSpeed({piles}, {h}) == {expected_result}")
        return test_case_generator_results

    def minEatingSpeed(self, piles, h):
        left, right = 1, int(1e9)
        while left < right:
            mid = (left + right) >> 1
            s = sum((x + mid - 1) // mid for x in piles)
            if s <= h:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    num_tests = 100
    solution = Solution()
    test_case_generator_results = solution.test_generated_test_cases(num_tests)
