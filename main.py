from fastapi import FastAPI
from pydantic import BaseModel
from agentes.agente_basico import graph
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