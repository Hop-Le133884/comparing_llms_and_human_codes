# hard_kthSmallest.py

import heapq

class LLM_Solution:
    def kthSmallest(self, mat, k):
        m, n = len(mat), len(mat[0])
        
        # Start with the first row, since we have to select one element from each row
        min_heap = [(sum(row[0] for row in mat), [0] * m)]  # (sum, indices of the selected elements)
        seen = set(tuple([0] * m))  # Set to track visited index combinations
        
        for _ in range(k - 1):  # We need to pop k-1 smallest sums
            curr_sum, indices = heapq.heappop(min_heap)
            
            # Generate new indices combinations by moving one element forward in each row
            for i in range(m):
                if indices[i] + 1 < n:
                    new_indices = list(indices)
                    new_indices[i] += 1
                    new_sum = curr_sum - mat[i][indices[i]] + mat[i][new_indices[i]]
                    if tuple(new_indices) not in seen:
                        seen.add(tuple(new_indices))
                        heapq.heappush(min_heap, (new_sum, new_indices))
        
        return heapq.heappop(min_heap)[0]
