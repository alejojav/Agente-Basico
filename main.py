from fastapi import FastAPI
from pydantic import BaseModel
from agentes.agente_basico import graph, graph2
from langchain_core.messages import HumanMessage

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

# schema
class AgenteBasico(BaseModel):
    prompt: str

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
    pass