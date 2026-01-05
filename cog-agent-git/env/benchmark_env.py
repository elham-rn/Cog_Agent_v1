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


def evaluate_action(env: str, action: str, goal: str) -> bool:

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
    if "Stabilize" in action and env in ["Security Breach", "Customer Crisis"]:
        return True
    
    keywords = SUCCESS_KEYWORDS.get(env, [])
    env_ok = any(k in action for k in keywords)
    goal = goal.lower()

    goal_conflict = False

    if "retain" in goal or "customer" in goal:
        goal_conflict = not any(k in action for k in ["call", "offer", "apolog", "retain"])

    elif "ship" in goal or "deliver" in goal:
        goal_conflict = not any(k in action for k in ["deploy", "release", "ship", "mvp"])

    elif "stabilize" in goal or "crisis" in goal:
        goal_conflict = not any(k in action for k in ["patch", "contain", "hotfix", "escalate"])
    if env_ok and not goal_conflict:
        return True

    if env_ok and goal_conflict:
        return random.random() < 0.3  # penalty for goal misalignment

    return False

   


