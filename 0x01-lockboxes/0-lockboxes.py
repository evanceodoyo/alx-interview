#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened
    Args:
        boxes: list of lists
    Returns:
        True if all boxes can be opened, False otherwise.
    """
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            print(f"new_key {new_key}")
            print(f"Boxes key {boxes[key]}")
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)

    print(f"keys {keys}")
    if len(keys) == len(boxes):
        return True
    return False
