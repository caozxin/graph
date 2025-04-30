from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        next_digit = {**{str(i): str(i + 1) for i in range(9)}, "9": "0"}
        prev_digit = {e: n for n, e in next_digit.items()}

    # def num_steps(target_combo: str, trapped_combos: list[str]) -> int:
        target_combo = target
        trapped_combos = deadends
        if target_combo == "0000":
            return 0
        trapped_combo_set = set(trapped_combos)
        steps = {"0000": 0}
        bfs_queue = deque(["0000"])

        while bfs_queue:
            top = bfs_queue.popleft()
            for i in range(4):
                new_combo = top[0:i] + next_digit[top[i]] + top[i + 1 :]
                if new_combo not in trapped_combo_set and new_combo not in steps:
                    bfs_queue.append(new_combo)
                    steps[new_combo] = steps[top] + 1
                    if new_combo == target_combo:
                        return steps[new_combo]
                new_combo = top[0:i] + prev_digit[top[i]] + top[i + 1 :]
                if new_combo not in trapped_combo_set and new_combo not in steps:
                    bfs_queue.append(new_combo)
                    steps[new_combo] = steps[top] + 1
                    if new_combo == target_combo:
                        return steps[new_combo]
        return -1
