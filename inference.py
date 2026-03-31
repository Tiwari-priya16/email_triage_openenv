import os
import json
from openai import OpenAI
from openenv.core import create_llm_client  # ✅ FIXED
from models import TriageAction

# ---------------- CONFIG ----------------
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
HF_TOKEN = os.getenv("HF_TOKEN") or os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Meta-Llama-3.1-8B-Instruct")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

# ✅ CORRECT HF SPACE URL
BASE_URL = "https://priyatiwari16-email-triage-openenv.hf.space"

# ✅ FIXED CLIENT
env_client = create_llm_client(base_url=BASE_URL)

TASKS = ["easy", "medium", "hard"]
MAX_STEPS = 15

# ---------------- LLM ----------------
def get_llm_action(obs):
    prompt = f"""
You are an expert email triage agent.

Email:
{obs.model_dump_json(indent=2)}

Return ONLY valid JSON matching TriageAction schema.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=300,
    )

    try:
        action_dict = json.loads(response.choices[0].message.content)
        return TriageAction(**action_dict)
    except:
        return TriageAction(category="spam", priority="low", action_type="archive")

# ---------------- RUN ----------------
scores = {}

for task in TASKS:
    obs = env_client.reset(task=task)
    total_reward = 0.0
    steps = 0

    while not obs.done and steps < MAX_STEPS:
        action = get_llm_action(obs)
        obs = env_client.step(action)
        total_reward += obs.reward
        steps += 1

    score = env_client.get_task_score(task)
    scores[task] = score
    print(f"Task {task}: score = {score:.2f}")

print("FINAL BASELINE SCORES:", scores)
print("AVERAGE:", sum(scores.values()) / len(scores))