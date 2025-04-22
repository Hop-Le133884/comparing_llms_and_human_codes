import bisect
class LLM_Solution:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        left = bisect.bisect_right(self.hits, timestamp - 300)
        right = len(self.hits)
        return right - left