# Island Perimeter
The goal of the project is calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers.

## Tasks

**0. Island Perimeter**


- `grid` is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

```
odo@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

odo@ubuntu:~/0x09$ 
odo@ubuntu:~/0x09$ ./0-main.py
12
odo@ubuntu:~/0x09$ 
```