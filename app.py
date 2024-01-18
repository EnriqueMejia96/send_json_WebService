from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pyngrok import ngrok

app = FastAPI()

# Definir el modelo de datos para la solicitud
class User(BaseModel):
    name: str  # Nombre del usuario
    email: str  # Correo electrónico del usuario

@app.post("/home")
def home():
  return 'Hola mundo'

@app.post("/users")
def add_user(user: User):
    # Procesar los datos (aquí puedes integrar tu lógica)
    # Para demostración, simplemente imprimiremos y devolveremos los datos
    print(f"Usuario recibido: {user.name}, Email: {user.email}")

    # Devolver una respuesta
    return {"message": "Usuario agregado exitosamente", "user": user.dict()}
