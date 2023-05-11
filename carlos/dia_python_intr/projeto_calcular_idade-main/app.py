#instalar o fastapi, pelo comando pip install fastapi
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = "*",
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def ola_mundo():
    return ler_arquivo()
def ler_arquivo():
    with open("arquivo.json", 'r') as dado:
        try:
            lista = list(json.load(dado))
            return lista 
        except:
            return []
        finally:
            dado.close()

  
#instalar uvicorn, utilzando pip install uvicorn
#para iniciar o uvicorn, digitar uvincorn no prompt ou digite no prompt python -m uvicorn app:app
