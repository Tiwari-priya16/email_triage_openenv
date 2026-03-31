SmartEmailTriage-OpenEnv 🔥

Winner-ready RL environment for enterprise email triage — built for Meta PyTorch OpenEnv Hackathon Round 1.

---

🚀 Motivation

Real companies lose hours every day due to email overload.
This environment trains agents to triage emails like a professional executive assistant — considering urgency, context, threads, and limited attention.

---

🧠 Action & Observation Spaces

- Observation
  Email (subject, sender, body snippet, timestamp, thread_id, sender_reputation)

- Action
  Structured triage:
  
  - category (work / personal / spam)
  - priority (high / medium / low)
  - action_type (archive / reply / forward / route / escalate)
  - optional fields (folder, reply_draft, forward_to)

---

📊 Tasks (Easy → Medium → Hard)

1. Easy — Single email triage
2. Medium — Thread-aware batch of 5 emails
3. Hard — 10-email inbox with deadlines + attention budget

---

📈 Baseline Scores

- Easy: 0.96
- Medium: 0.89
- Hard: 0.76
- Average: 0.87

---

⚙️ Setup

pip install -r requirements.txt

---

🐳 Run with Docker

docker build -t email-triage-env .
docker run -p 8000:8000 email-triage-env

---

🧪 Run Inference

python inference.py

---

🌐 Live API

👉 https://priyatiwari16-email-triage-openenv.hf.space

---

🏆 Goal

Maximize triage accuracy and decision efficiency using LLM-based agents.
