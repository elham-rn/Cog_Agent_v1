from collections import deque
import time


class ShortTermMemory:
    def __init__(self, window: int, decay: float):
        self.window = window
        self.decay = decay
        self.items = deque(maxlen=window)

    def add(self, env, task, action, outcome, goal):
        self.items.append({
            "env": env,
            "task": task,
            "action": action,
            "outcome": outcome,
            "goal": goal,
            "ts": time.time()
        })
