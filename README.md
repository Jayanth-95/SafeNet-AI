# SafeNet-AI
Agentic AI system for real-time scam detection using NLP, behavioral analysis, and multi-agent cybersecurity intelligence.
## Project Structure

```
SafeNet-AI
│
├── agents
│   ├── message_agent.py
│   ├── url_agent.py
│   └── behavior_agent.py
│
├── api
│   └── server.py
│
├── models
│   └── phishing_model.py
│
├── data
│   └── sample_messages.csv
│
├── main.py
├── requirements.txt
└── README.md
```
## Agentic AI Architecture

SafeNet AI uses a **multi-agent system** where specialized AI agents collaborate to detect scams and protect users in real time.

### Message Analysis Agent
Uses Natural Language Processing (NLP) to analyze messages and detect phishing patterns such as urgent requests, fake financial instructions, and suspicious language.

### URL Verification Agent
Examines suspicious URLs and checks for malicious domains, phishing structures, and known scam indicators.

### Behavior Monitoring Agent
Analyzes user interaction patterns and detects abnormal activities that may indicate fraud or social engineering attacks.

### Decision Agent
Combines insights from all agents to calculate a **risk score** and determines whether the system should warn the user or flag the message as malicious.

This multi-agent collaboration enables SafeNet AI to function as an **autonomous digital security assistant**, proactively preventing scams before users interact with malicious content.
