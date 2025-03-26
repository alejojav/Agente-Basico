from langgraph.prebuilt import create_react_agent
from core.config import model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from agentes.tools import tavily_search_tool

# tools
tools = [tavily_search_tool]

# graph basico
graph = create_react_agent(model, tools=tools)

# grahp2
system_prompt = """
Eres un agente experto en deportes, te llamas TriplePlay, tus funciones son:

- buscar información sobre deportes: utilizando la herramienta de búsqueda de Tavily
- generar un resumen de deportes: utilizando la api de tavily 

tus respuestas deben ser cortas y precisas, con informacion relevante
"""

chat_template_prompt =  ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=system_prompt),
        MessagesPlaceholder(variable_name = "messages"),
    ]
)

graph2 = create_react_agent(
    model,
    tools=tools,
    prompt=system_prompt,
    # state
    # memoria
)
