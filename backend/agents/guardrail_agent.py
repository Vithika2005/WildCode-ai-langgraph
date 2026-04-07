
def guardrail_agent(text):

    if not text or len(text) < 20:
        return {"guardrail": "⚠️ Weak response"}

    bad_words = ["maybe", "possibly", "might"]

    for word in bad_words:
        if word in text.lower():
            return {"guardrail": "⚠️ Low confidence"}

    return {"guardrail": "Safe"}
