import random


ENVIRONMENTS = [
    "Normal Operations",
    "Customer Crisis",
    "Team Delay",
    "Competitor Launch",
    "Negative Feedback",
    "Budget Cut",
    "Security Breach",
    "Regulatory Change",
]

TASKS = [
    "Customer threatens to cancel subscription",
    "Negative feedback goes viral",
    "Team missed internal deadline",
    "Competitor launched aggressive pricing",
    "Unexpected budget reduction",
    "Security incident detected",
    "New regulation announced",
]


def sample_env_task():
    env = random.choice(ENVIRONMENTS)
    task = random.choice(TASKS)
    return env, task


def evaluate_action(env: str, action: str) -> bool:
    """
    Very lightweight success model.
    This is intentionally simple and deterministic enough
    for reproducible benchmarking.
    """
    action = action.lower()

    SUCCESS_KEYWORDS = {
        "Customer Crisis": ["call", "apolog", "retain", "offer"],
        "Negative Feedback": ["respond", "acknowledge", "fix"],
        "Team Delay": ["reassign", "plan", "prioritize"],
        "Competitor Launch": ["analyze", "adjust", "differentiate"],
        "Security Breach": ["patch", "audit", "contain"],
    }

    keywords = SUCCESS_KEYWORDS.get(env, [])
    return any(k in action for k in keywords)
