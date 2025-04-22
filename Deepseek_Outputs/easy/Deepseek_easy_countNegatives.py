class LLM_Solution:
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        row = 0
        col = cols - 1
        
        while row < rows and col >= 0:
            if grid[row][col] < 0:
                count += (rows - row)
                col -= 1
            else:
                row += 1
        return count