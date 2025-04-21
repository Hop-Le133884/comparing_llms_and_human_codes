# hard_kIncreasing.py

class LLM_Solution:
    def kIncreasing(self, arr: list[int], k: int) -> int:
        """
        Minimum Operations to Make the Array K-increasing
        """

        def longest_non_decreasing_subsequence(sub_arr):
            tails = []
            for num in sub_arr:
                if not tails or num >= tails[-1]:
                    tails.append(num)
                else:
                    l, r = 0, len(tails) - 1
                    while l < r:
                        mid = l + (r - l) // 2
                        if tails[mid] <= num:
                            l = mid + 1
                        else:
                            r = mid
                    tails[l] = num
            return len(tails)

        n = len(arr)
        ans = 0
        for i in range(k):
            sub_arr = [arr[j] for j in range(i, n, k)]
            ans += len(sub_arr) - longest_non_decreasing_subsequence(sub_arr)
        return ans