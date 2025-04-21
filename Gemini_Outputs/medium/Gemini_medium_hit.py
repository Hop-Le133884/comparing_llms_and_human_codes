from collections import deque

class LLM_Solution:
    def __init__(self):
        """
        Design Hit Counter
        """
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        """
        Records a hit that happened at timestamp (in seconds).
        Several hits may happen at the same timestamp.
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
        """
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        return len(self.hits)