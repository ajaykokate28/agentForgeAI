from langgraph.graph import StateGraph, START, END
from app.graph.state import SupportState
from app.graph.nodes import classify_intent

def build_support_graph():

    # Create the graph
    builder = StateGraph(SupportState)

    # Register the classification node
    builder.add_node("classify_intent", classify_intent)

    # Connect START to classification
    builder.add_edge(START, "classify_intent")

    # Connect classification to END
    builder.add_edge("classify_intent", END)

    # Compile the graph
    graph = builder.compile()

    return graph