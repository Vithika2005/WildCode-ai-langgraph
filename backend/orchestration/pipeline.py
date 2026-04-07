from orchestration.graph import build_graph

graph = build_graph()

def run_pipeline():
    result = graph.invoke({})
    return result["report"]
