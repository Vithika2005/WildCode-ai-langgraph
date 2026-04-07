
from tools.ollama_tool import ask_ollama

def report_agent(data):
    """
    data contains:
    {
        "data": combined sensor output,
        "analysis": analyst output,
        "guard": guardrail result
    }
    """

    prompt = f"""
You are Aaranyak-AI Report Generator.

Convert the given system outputs into a clean, structured forest monitoring report.

INPUT:
{data}

RULES:
- Be clear and professional
- No repetition
- No guessing missing values
- Keep it concise
- Highlight critical alerts first

OUTPUT FORMAT:

🚨 Alerts:
- <critical alerts>

📊 Environment:
- Temperature: <value>
- Humidity: <value>

🧠 Analysis Summary:
<short summary>

⚠️ Risks:
- <risk points>

✅ Recommended Actions:
- <actions>
"""

    report = ask_ollama(prompt)

    return {
        "final_report": report,
        "raw_data": data
    }
