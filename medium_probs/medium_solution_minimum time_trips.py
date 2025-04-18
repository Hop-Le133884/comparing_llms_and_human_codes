
import random

class Solution:
    def minimumTime(self, time, totalTrips):
        mx = min(time) * totalTrips
        return bisect_left(
            range(mx), totalTrips, key=lambda x: sum(x // v for v in time)
        )
        
