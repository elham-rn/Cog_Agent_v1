import networkx as nx


class SemanticMemory:
    def __init__(self, ema_decay: float, similarity_threshold: float):
        self.graph = nx.DiGraph()
        self.decay = ema_decay
        self.threshold = similarity_threshold

    def update(self, episodes):
        for ep in episodes:
            u, v = ep.env, ep.action
            w = 1.0 if ep.outcome == "success" else -1.0
            prev = self.graph.get_edge_data(u, v, {}).get("weight", 0.0)
            new_w = prev * self.decay + w * (1 - self.decay)
            self.graph.add_edge(u, v, weight=new_w)
