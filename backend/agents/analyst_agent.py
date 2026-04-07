
from tools.ollama_tool import ask_ollama

def analyst_agent(data):

    prompt = f"""
You are Aaranyak-AI, a forest monitoring intelligence system.

Analyze the following real-time data and give STRICT structured output.

DATA:
{data}

INSTRUCTIONS:
- Be precise
- No storytelling
- No guessing missing values
- Focus on safety and anomalies

OUTPUT FORMAT:

Summary:
<one line status>

Risks:
- <risk 1>
- <risk 2>

Recommendations:
- <action 1>
- <action 2>
"""

    result = ask_ollama(prompt)

    return {"analysis": result}
