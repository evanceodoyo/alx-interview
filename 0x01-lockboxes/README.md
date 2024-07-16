# Lockboxes

This repository contains the Python script [`0-lockboxes.py`](./0-lockboxes.py) that implements a solution to a lockboxes problem.

## Problem Description

The lockboxes problem involves a set of lockboxes, each containing a list of keys. The goal is to determine if it is possible to unlock all the lockboxes by using the keys inside them.

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
    - There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

## Approach

The script uses a depth-first search algorithm to explore the lockboxes and their corresponding keys. It keeps track of the visited lockboxes to avoid revisiting them.

## Example Usage

Here is an example of how to use the script (main.py):

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
```

Execution and expected results:
```
$ ./main.py
True
True
False
```