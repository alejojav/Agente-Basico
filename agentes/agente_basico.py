from langgraph.prebuilt import create_react_agent
from core.config import model
from agentes.tools import tavily_search_tool

# tools
tools = [tavily_search_tool]

graph = create_react_agent(
    model,
    tools=tools,
)

