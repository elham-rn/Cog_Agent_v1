import yaml
import numpy as np

from agent.cognitive_agent import CognitiveAgent
from env.benchmark_env import sample_env_task, evaluate_action
from utils.seeding import set_global_seed
from utils.metrics import success_rate


SEEDS = [11, 23, 42, 77, 99]


def run_once(config, seed):
    config = dict(config)
    config["seed"] = seed

    set_global_seed(seed)
    agent = CognitiveAgent(config)

    for _ in range(config["episodes"]):
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
        success = evaluate_action(env, action)
        agent.run(env, task, action, success)
        if "Stabilize" in agent.goal:
            action = "contain issue and minimize risk"
        else:
            action = ACTION_MAP.get(env, "monitor situation")        

    return success_rate(agent.history)


def main():
    with open("config/default.yaml", "r") as f:
        config = yaml.safe_load(f)

    results = []
    for seed in SEEDS:
        rate = run_once(config, seed)
        results.append(rate)
        print(f"Seed {seed}: success rate = {rate:.3f}")

    print("\nMULTI-SEED SUMMARY")
    print(f"Mean: {np.mean(results):.3f}")
    print(f"Std : {np.std(results):.3f}")


if __name__ == "__main__":
    main()
