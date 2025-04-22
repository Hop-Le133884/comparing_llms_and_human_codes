class LLM_Solution:
    def preimageSizeFZF(self, k):
        def zeta(x):
            res = 0
            while x > 0:
                x = x // 5
                res += x
            return res
        
        left, right = 0, 5 * (k + 1)
        while left <= right:
            mid = (left + right) // 2
            zeros = zeta(mid)
            if zeros == k:
                return 5
            elif zeros < k:
                left = mid + 1
            else:
                right = mid - 1
        return 0