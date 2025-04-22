class LLM_Solution:
    def minmaxGasDist(self, stations, k):
        left, right = 0, stations[-1] - stations[0]
        while right - left > 1e-6:
            mid = (left + right) / 2
            count = 0
            for i in range(len(stations) - 1):
                count += int((stations[i+1] - stations[i]) / mid)
            if count <= k:
                right = mid
            else:
                left = mid
        return left