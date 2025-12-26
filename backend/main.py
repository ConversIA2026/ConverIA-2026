# Punto de entrada de la aplicación
# Solo orquestación, nada de lógica de negocio 

from fastapi import FastAPI
from app.api.routes import router 


app = FastAPI(title="ConversIA Backend", version="1.0.0")
app.include_router(router, prefix="/api")