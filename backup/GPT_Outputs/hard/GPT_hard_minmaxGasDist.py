# hard_minmaxGasDist.py

class LLM_Solution:
    def minmaxGasDist(self, stations, k):
        def canAddStations(maxDist):
            count = 0
            for i in range(1, len(stations)):
                # Calculate the number of stations to add between two adjacent stations
                count += (stations[i] - stations[i-1] - 1) // maxDist
                if count > k:
                    return False
            return True

        left, right = 0.0, (stations[-1] - stations[0]) / k  # Initial bounds for the maximum distance

        while right - left > 1e-6:  # Precision of 10^-6
            mid = (left + right) / 2
            if canAddStations(mid):
                right = mid
            else:
                left = mid

        return left
