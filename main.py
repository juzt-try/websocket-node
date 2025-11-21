from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Permitir conexiones desde cualquier origen (para pruebas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clients: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    print("Cliente conectado")

    try:
        while True:
            msg = await ws.receive_text()
            print("Mensaje recibido:", msg)

            # reenviar a todos
            for client in clients:
                await client.send_text(msg)

    except Exception as e:
        print("Cliente desconectado")
        clients.remove(ws)
