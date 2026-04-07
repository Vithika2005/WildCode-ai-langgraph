from langgraph.graph import StateGraph
from typing import TypedDict

# 🔌 Agents
from tools.firebase_tool import get_sensor_data
from agents.alert_agent import alert_agent
from agents.env_agent import env_agent
from agents.fencing_agent import fencing_agent
from agents.audio_agent import audio_agent
from agents.analyst_agent import analyst_agent
from agents.guardrail_agent import guardrail_agent
from agents.report_agent import report_agent


# 🧠 STATE
class GraphState(TypedDict):
    data: dict
    combined: dict
    analysis: dict
    guard: dict
    report: dict


# 🧱 NODES

def fetch_data(state):
    data = get_sensor_data()
    print("🔥 Firebase:", data)
    return {"data": data}


def run_agents(state):
    data = state["data"]

    alert = alert_agent(data)
    env = env_agent(data)
    fence = fencing_agent(data)
    audio = audio_agent()

    combined = {
        **alert,
        **env,
        **fence,
        **audio
    }

    return {"combined": combined}


def analyze(state):
    analysis = analyst_agent(state["combined"])
    return {"analysis": analysis}


def guard(state):
    g = guardrail_agent(state["analysis"]["analysis"])
    return {"guard": g}


def report(state):
    r = report_agent({
        "data": state["combined"],
        "analysis": state["analysis"],
        "guard": state["guard"]
    })

    return {"report": r}


# 🚀 BUILD GRAPH

def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("fetch", fetch_data)
    graph.add_node("agents", run_agents)
    graph.add_node("analyze", analyze)
    graph.add_node("guard", guard)
    graph.add_node("report", report)

    graph.set_entry_point("fetch")

    graph.add_edge("fetch", "agents")
    graph.add_edge("agents", "analyze")
    graph.add_edge("analyze", "guard")
    graph.add_edge("guard", "report")

    graph.set_finish_point("report")

    return graph.compile()
