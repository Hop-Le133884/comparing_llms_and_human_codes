# hard_preimageSizeFZF.py

class LLM_Solution:
    def preimageSizeFZF(self, k):
        # Function to count how many trailing zeroes are there in factorial of x
        def count_zeroes(x):
            count = 0
            while x >= 5:
                x //= 5
                count += x
            return count

        # Binary search for the range where f(x) == k
        left, right = 0, 5 * (k + 1)
        
        # Finding the first number whose factorial has at least 'k' trailing zeroes
        while left < right:
            mid = (left + right) // 2
            if count_zeroes(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        # Now 'left' is the first number where f(x) >= k
        first = left
        if count_zeroes(first) != k:
            return 0
        
        # Finding the first number whose factorial has more than 'k' trailing zeroes
        right = 5 * (k + 1)
        left = first
        while left < right:
            mid = (left + right) // 2
            if count_zeroes(mid) > k:
                right = mid
            else:
                left = mid + 1
        
        # The range where f(x) == k will be [first, left - 1], so the size of the range is left - first
        return left - first
