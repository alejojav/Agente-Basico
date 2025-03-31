from fastapi import FastAPI
from agentes.agente_basico import graph, graph2, graph3
from langchain_core.messages import HumanMessage
from schemas.schema import AgenteBasico

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

# schema


@app.post("/agente-basico")
async def agente_basico(prompt: AgenteBasico):

    inputs = [HumanMessage(content=prompt.prompt)]
    inputs = {"messages": inputs}
    response = graph.invoke(inputs)
    messages = response["messages"][-1].content
    return {
        "response": messages,
    }

@app.post("/agente-basico-2")
def agente_basico_2(prompt: AgenteBasico):
    #crear una lista de mensajes
    #asignar el mensaje de entrada, usuario
    user_input = [HumanMessage(content=prompt.prompt)]

    #estado inicial de nuestro
    user_input = {"messages": user_input}

    #invocar la funcion de la graph2 -> agente
    response = graph2.invoke(user_input)

    #obtener el ultimo mensaje de la respuesta aimessages
    messages = response["messages"][-1].content
    return {
        "response": messages,
    }

@app.post("/agente-basico-3")
async def agente_basico_3(prompt: AgenteBasico):
    user_input = [HumanMessage(content=prompt.prompt)]

    user_input = {"messages": user_input}

    config = {"configurable": {"thread_id": prompt.user_id}}

    response = graph3.invoke(user_input, config)
    messages = response["messages"][-1].content
    return {
        "response": messages,
    }