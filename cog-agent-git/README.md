# Cog-Agent: A Cognitive LLM Agent with Long-Term Memory and Adaptive Goal Revision

This repository provides a **minimal and reproducible implementation** of the Cog-Agent framework evaluated in the accompanying paper:

> *A Cognitive Framework for LLM-based Agents with Long-Term Memory and Adaptive Goal Revision*  
> (submitted to an IEEE international conference)

The code is intended **for research reproducibility**, not as a production system or interactive demo.

---

## Overview

Cog-Agent is a cognitive agent architecture that integrates:

- Episodic memory (experience-level storage)
- Semantic memory (abstracted environment–action associations)
- Short-term working memory
- A reinforcement learning–based **Goal Meta-Controller** for adaptive goal revision

The key contribution of this work is demonstrating that **goal-level adaptation** enables sustained long-term learning and prevents early performance saturation.

---

## Repository Scope (Important)

This repository includes:
- Core agent logic
- Experimental scripts used to generate results in the paper
- Configuration files for full and ablated models

This repository **does NOT include**:
- Streamlit or interactive UI code
- Visualization dashboards
- API keys or proprietary services

---

## Installation

Tested with Python **3.10+**.

```bash
git clone https://github.com/elham-rn/Cog_Agent_v1
cd cog-agent
pip install -r requirements.txt

## Reproducing the Main Results
Full Cog-Agent (with Goal Meta-Controller)
python experiments/run_full.py

## Ablation: Cog-Agent without Goal Meta-Controller
python experiments/run_ablation_no_goal.py


## Multi-seed Evaluation (mean ± std)
python experiments/run_multi_seed.py

The above scripts reproduce the aggregate results reported in Table 4 (Ablation Analysis) of the paper.

##Results
The results reported in the paper are obtained by running the agent for multiple random seeds and aggregating success rates.
Aggregated results (mean ± std over multiple seeds) are provided in:
results/summary_table.csv
results/seeds_mean_std.csv


