class LLM_Solution:
    def reachNumber(self, target: int) -> int:
        """
        Reach a Number

        You are standing at position 0 on an infinite number line. There is a destination at position target.
        You can make some number of moves numMoves so that:
        - On each move, you can either go left or right.
        - During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.
        Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves)
        to reach the destination.
        """
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        if target % 2 == 0:
            return k
        else:
            return k + 1 + k % 2