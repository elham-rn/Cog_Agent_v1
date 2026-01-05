from typing import List, Dict, Any
import time
import numpy as np

from agent.memory_stm import ShortTermMemory
from agent.memory_episodic import EpisodicMemory, Episode
from agent.memory_semantic import SemanticMemory
from agent.goal_policy import GoalPolicy


class CognitiveAgent:
    def __init__(self, config: dict):
        self.config = config
        self.goal = config["agent"]["initial_goal"]

        self.short_term = ShortTermMemory(**config["memory"]["short_term"])
        self.episodic = EpisodicMemory(config["memory"]["episodic"]["embedding_dim"])
        self.semantic = SemanticMemory(**config["memory"]["semantic"])

        self.goal_policy = GoalPolicy(self, config)
        self.history: List[Dict[str, Any]] = []
        self.step = 0

    def run(self, env: str, task: str, action: str, success: bool):
        ep = Episode(
            step=self.step,
            goal=self.goal,
            env=env,
            task=task,
            action=action,
            outcome="success" if success else "failure",
            timestamp=time.time(),
        )

        self.short_term.add(env, task, action, ep.outcome, self.goal)
        self.episodic.add(ep)
        self.semantic.update([ep])

        if self.goal_policy.enabled and self.step % self.goal_policy.interval == 0:
            new_goal = self.goal_policy.maybe_update_goal()
            if new_goal:
                self.goal = new_goal

        self.history.append({
            "step": self.step,
            "success": success,
            "goal": self.goal
        })
        self.step += 1
