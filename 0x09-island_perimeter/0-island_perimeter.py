#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Calculates and returns the perimeter of the island described in `grid`.

    Args:
      grid (List[int]): rectangular representation of the island with:
      - 0 representing water
      - 1 representing land
      - Each cell is square, with a side of length 1
      - Cells are connected horizontally/vertically (not diagonally)
      - width and height not exceeding 100
    """
    visited = set()

    def dfs(row, col):
        """Search for land cells using depth first seach.
        Args:
          row: Row on the grid.
          col: Column on the grid.

        Returns: Perimeter of the island.
        """
        if row >= len(grid) or col >= len(
                grid[0]) or grid[row][col] == 0 or row < 0 or col < 0:
            return 1

        if (row, col) in visited:
            return 0

        visited.add((row, col))
        perimeter = dfs(row, col)
        perimeter += dfs(row, col + 1)
        perimeter += dfs(row, col - 1)
        perimeter += dfs(row - 1, col)
        perimeter += dfs(row + 1, col)
        return perimeter

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return dfs(row, col)
