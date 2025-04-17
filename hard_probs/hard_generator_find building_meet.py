
import random

class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        n, m = len(heights), len(queries)
        for i in range(m):
            queries[i] = [min(queries[i]), max(queries[i])]
        j = n - 1
        s = sorted(set(heights))
        ans = [-1] * m
        
        class BinaryIndexedTree:
            __slots__ = ["n", "c"]

            def __init__(self, n: int):
                self.n = n
                self.c = [float("inf")] * (n + 1)

            def update(self, x: int, v: int):
                while x <= self.n:
                    self.c[x] = min(self.c[x], v)
                    x += x & -x

            def query(self, x: int) -> int:
                mi = float("inf")
                while x:
                    mi = min(mi, self.c[x])
                    x -= x & -x
                return -1 if mi == float("inf") else mi
        
        tree = BinaryIndexedTree(n)
        for i in sorted(range(m), key=lambda i: -queries[i][1]):
            l, r = queries[i]
            while j > r:
                k = n - bisect_left(s, heights[j]) + 1
                tree.update(k, j)
                j -= 1
            if l == r or heights[l] < heights[r]:
                ans[i] = r
            else:
                k = n - bisect_left(s, heights[l])
                ans[i] = tree.query(k)
        return ans

def generate_test_case():
    solution = Solution()

    # Generate random heights list
    n = random.randint(2, 1001)
    heights = [random.randint(1, 10**9) for _ in range(n)]

    # Generate random queries list
    m = random.randint(1, 101)
    queries = []
    for _ in range(m):
        l = random.randint(0, n - 1)
        r = random.randint(l, n - 1)
        queries.append([l, r])

    # Calculate the expected result using the provided Solution class
    expected_result = solution.leftmostBuildingQueries(heights, queries)

    return heights, queries, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        heights, queries, expected_result = generate_test_case()
        solution = Solution()
        assert solution.leftmostBuildingQueries(heights, queries) == expected_result
        print(f"assert solution.leftmostBuildingQueries({heights}, {queries}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.leftmostBuildingQueries({heights}, {queries}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
