import yaml

from agent.cognitive_agent import CognitiveAgent
from env.benchmark_env import sample_env_task, evaluate_action
from utils.seeding import set_global_seed
from utils.metrics import summary


def main():
    with open("config/ablation_no_goal.yaml", "r") as f:
        config = yaml.safe_load(f)

    set_global_seed(config["seed"])

    agent = CognitiveAgent(config)
    episodes = config["episodes"]

    for _ in range(episodes):
        env, task = sample_env_task()

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

        action = ACTION_MAP.get(env, "monitor situation")

        success = evaluate_action(env, action, "generic execution")


        agent.run(env, task, action, success)
        if "Stabilize" in agent.goal:
            action = "contain issue and minimize risk"
        else:
            action = ACTION_MAP.get(env, "monitor situation")

    print("ABLATION (NO GOAL META-CONTROLLER) RESULTS")
    print(summary(agent.history))


if __name__ == "__main__":
    main()
