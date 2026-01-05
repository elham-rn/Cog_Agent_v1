import random


class GoalPolicy:
    def __init__(self, agent, config: dict):
        self.agent = agent
        self.enabled = config["agent"]["use_goal_meta_controller"]
        self.interval = config["agent"]["goal_revision_interval"]
        self.goal_history = [agent.goal]

    def maybe_update_goal(self):
        if not self.enabled:
            return None

        recent = self.agent.history[-20:]
        if not recent:
            return None

        success_rate = sum(r["success"] for r in recent) / len(recent)
        if success_rate < 0.4:
            new_goal = "Stabilize system before pursuing original objective"
            self.goal_history.append(new_goal)
            return new_goal

        return None
