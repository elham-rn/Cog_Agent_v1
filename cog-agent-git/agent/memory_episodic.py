from dataclasses import dataclass
from typing import List
import numpy as np


@dataclass
class Episode:
    step: int
    goal: str
    env: str
    task: str
    action: str
    outcome: str
    timestamp: float


class EpisodicMemory:
    def __init__(self, dim: int):
        self.dim = dim
        self.episodes: List[Episode] = []

    def add(self, episode: Episode):
        self.episodes.append(episode)
