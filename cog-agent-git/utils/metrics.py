import numpy as np


def success_rate(history):
    if not history:
        return 0.0
    return np.mean([1 if h["success"] else 0 for h in history])


def rolling_success(history, window: int = 50):
    values = [1 if h["success"] else 0 for h in history]
    out = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        out.append(sum(values[start:i+1]) / (i - start + 1))
    return out


def summary(history):
    return {
        "total_steps": len(history),
        "success_rate": success_rate(history),
    }
