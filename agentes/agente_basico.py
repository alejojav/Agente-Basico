from langgraph.prebuilt import create_react_agent
from core.config import model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import MessagesState
from langgraph.managed import IsLastStep
from langchain_core.messages import BaseMessage
from typing import Annotated, TypedDict, Optional
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import MemorySaver

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

# Agente 3
system_prompt3 = """
Eres un agente experto en cocinas, te llamas ChefTorta, tus funciones son:

- buscar recetas: utilizando la Api de Tavily para buscar recetas.
- generar un resumen de las recetas: utilizando la informacion obtenida de la API de tavily.
- indica los pasos a seguir para preparar la receta con la informacion obtenida de la API de tavily.
- muestra la respuesta final en formato markdown.

tus respuestas deben ser cortas y precisas, con informacion relevante.
no icluyas informacion que no este relacionada con el tema.
"""

chat_template_prompt_3 =  ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=system_prompt3),
        MessagesPlaceholder(variable_name = "messages"),
    ]
)

#state
#class CustomState(MessagesState):
#    remaining_steps: IsLastStep
class CustomState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    is_last_step: IsLastStep
    remaining_steps: Optional[int] = None

#graph
graph3 = create_react_agent(
    model,
    tools=tools,
    prompt=chat_template_prompt_3,
    state_schema=CustomState,
    checkpointer=MemorySaver()   
)