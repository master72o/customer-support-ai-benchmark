# Customer Support AI Benchmark

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTest](https://img.shields.io/badge/PyTest-Passing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A specialized domain benchmark framework for evaluating customer support LLMs across 7 critical enterprise dimensions:

1. **Refund Reasoning & Eligibility Evaluation**
2. **Product Understanding & Troubleshooting**
3. **Enterprise Policy & Terms of Service Compliance**
4. **Tone, Empathy & Professional Communication**
5. **Multi-Constraint Instruction Following**
6. **Hallucination & Fake Policy Invention Detection**
7. **Human Escalation Trigger Identification**

---

## 📊 Benchmark Leaderboard Summary (Evaluated Models)

| Model Name | Overall Score (0-100) | Policy Compliance | Empathy Score | Hallucination Free | Human Escalation |
|---|---|---|---|---|---|
| 🥇 **SupportBot-Pro** | **94.2** | 96% | 95% | 98% | 95% |
| 🥈 **SupportBot-Lite** | **83.5** | 88% | 85% | 89% | 82% |
| 🥉 **Base-LLM-7B** | **71.0** | 72% | 75% | 68% | 65% |
| 4th **Legacy-Bot-v1** | **52.4** | 50% | 60% | 45% | 40% |

---

## 🛠️ Execution & CLI

```bash
# Run benchmark evaluation across all models
python cli.py run

# Generate visual breakdown charts
python cli.py plot

# Run PyTest unit tests
pytest tests/
```
