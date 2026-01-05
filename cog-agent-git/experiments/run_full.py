import yaml
from env.benchmark_env import sample_env_task, evaluate_action
from agent.cognitive_agent import CognitiveAgent
from utils.seeding import set_global_seed
from utils.metrics import summary


# Lightweight, deterministic action generator (LLM abstracted)
def select_action(env: str, goal: str) -> str:
    goal = goal.lower()

    if "customer" in goal:
        return "call customer and offer retention plan"

    if "stabilize" in goal or "crisis" in goal:
        return "contain issue and patch system"

    ACTION_MAP = {
        "Customer Crisis": "call customer and apologize",
        "Negative Feedback": "respond and acknowledge feedback",
        "Team Delay": "reassign tasks and prioritize",
        "Competitor Launch": "analyze competitor and adjust strategy",
        "Security Breach": "contain breach and patch system",
        "Budget Cut": "replan budget and reduce cost",
        "Regulatory Change": "review regulation and adapt process",
        "Normal Operations": "continue monitoring operations",
    }

    return ACTION_MAP.get(env, "monitor situation")


def main():
    with open("config/default.yaml", "r") as f:
        config = yaml.safe_load(f)

    set_global_seed(config["seed"])

    agent = CognitiveAgent(config)
    episodes = config["episodes"]

    for _ in range(episodes):
        env, task = sample_env_task()

        # 1️⃣ Agent observes context and may revise goal
        agent.observe(env, task)

        # 2️⃣ Action is selected conditioned on CURRENT goal
        action = select_action(env, agent.goal)

        # 3️⃣ Environment evaluates outcome (goal-aware)
        success = evaluate_action(env, action, agent.goal)

        # 4️⃣ Agent updates internal state & memory
        agent.update(env, task, action, success)

    print("FULL AGENT RESULTS")
    print(summary(agent.history))


if __name__ == "__main__":
    main()
