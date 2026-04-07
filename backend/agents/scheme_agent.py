# backend/agents/scheme_agent.py

from tools.ollama_tool import ask_ollama

def scheme_agent(query):
    prompt = f"Summarize Indian government schemes related to: {query}"
    return {"schemes": ask_ollama(prompt)}
