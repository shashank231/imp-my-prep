

from collections import deque

class Solution:
    def numIslands(self, grid):
        """
        Counts the number of islands in a 2D grid.
        Island = group of adjacent '1's connected horizontally or vertically.
        """

        # Edge case: empty grid
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        # BFS to mark all connected land from a starting cell
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            # All 4 possible directions
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    # Check bounds and if it's unvisited land
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == '1' and
                        (nr, nc) not in visited
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        island_count = 0

        # Traverse the full grid
        for r in range(rows):
            for c in range(cols):

                # Found unvisited land → new island
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    island_count += 1

        return island_count
