# hard_kthSmallest.py

import heapq

class LLM_Solution:
    def kthSmallest(self, mat: list[list[int]], k: int) -> int:
        """
        Find the Kth Smallest Sum of a Matrix With Sorted Rows
        """
        m = len(mat)
        pq = [(sum(row[0] for row in mat), [0] * m)]
        visited = {tuple([0] * m)}
        for _ in range(k - 1):
            curr_sum, curr_indices = heapq.heappop(pq)
            for i in range(m):
                next_indices = list(curr_indices)
                if next_indices[i] + 1 < len(mat[i]):
                    next_indices[i] += 1
                    next_sum = curr_sum - mat[i][curr_indices[i]] + mat[i][next_indices[i]]
                    next_indices_tuple = tuple(next_indices)
                    if next_indices_tuple not in visited:
                        heapq.heappush(pq, (next_sum, next_indices))
                        visited.add(next_indices_tuple)
        return pq[0][0]