import socket
import time

class TCP_Client:

    def __init__(self, nombreDelServer, puertoDelServer, ball, paddle_host, paddle_client, key_states):
        self.ip = nombreDelServer
        self.puerto = puertoDelServer
        self.jugador_conectado = False

        self.paddle_client = paddle_client
        self.paddle_host = paddle_host
        self.keys = key_states
        self.ball = ball

    def setup_keys(self, wn):
        self.wn = wn
        self.wn.listen()
        for key in self.keys:
            self.wn.onkeypress(lambda k=key: self.keys.update({k: True}), key)
            self.wn.onkeyrelease(lambda k=key: self.keys.update({k: False}), key)

    def iniciar(self):
        for i in range(20):
            try:
                self.clienteSocketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.clienteSocketTCP.connect((self.ip, self.puerto))
                self.jugador_conectado=True
                print("Conectado al servidor")
                break
            except ConnectionRefusedError:
                print(f"[Cliente] Conexión rechazada. Reintentando ({i+1}/{20})...")
                time.sleep(1)
        else:
            raise ConnectionRefusedError("No se pudo conectar con el servidor tras varios intentos.")

        try:
            datos = self.clienteSocketTCP.recv(1024).decode()
            parts = datos.split('|')

            self.ball.setx(float(parts[4]))
            self.ball.sety(float(parts[3]))

            while True:
                datos_envio = f"paddle_client|{self.paddle_client.ycor()}"
                self.clienteSocketTCP.send(datos_envio.encode())

                datos = self.clienteSocketTCP.recv(1024).decode()
                parts = datos.split('|')

                self.paddle_host.sety(float(parts[1]))

        except Exception as e:
            print("Error en comunicación:", e)

        finally:
            self.clienteSocketTCP.close()
            print("Conexión cerrada")



    def mover_paddles(self):
        if self.keys.get("w") and self.paddle_client.ycor() < 250:
            self.paddle_client.sety(self.paddle_client.ycor() + 3)
        if self.keys.get("s") and self.paddle_client.ycor() > -250:
            self.paddle_client.sety(self.paddle_client.ycor() - 3)