const express = require('express');
const http = require('http');
const WebSocket = require('ws');

const app = express();
const server = http.createServer(app);

const wss = new WebSocket.Server({ server });

wss.on('connection', (ws) => {
  console.log('Nueva conexión WebSocket');

  ws.on('message', (msg) => {
    console.log('Mensaje recibido:', msg.toString());

    // reenviar el mensaje a todos los clientes conectados
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(msg.toString());
      }
    });
  });

  ws.send('Conectado al servidor WebSocket');
});

// Puerto
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => console.log(`Servidor WebSocket en puerto ${PORT}`));
