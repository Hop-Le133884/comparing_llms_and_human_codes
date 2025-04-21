# hard_minmaxGasDist.py

class LLM_Solution:
    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        """
        Minimize Max Distance to Gas Station
        """
        def possible(x):
            added = 0
            for i in range(len(stations) - 1):
                added += int((stations[i+1] - stations[i]) / x)
            return added <= k

        left, right = 0, max(stations[i+1] - stations[i] for i in range(len(stations) - 1))
        while right - left > 1e-6:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return right