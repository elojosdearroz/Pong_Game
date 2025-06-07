import socket

class TCP_Server:

	def __init__(self, ip, puerto, ball, paddle_host, paddle_client, key_states):
		self.jugador_conectado = False

		self.ipServer = ip
		self.puertoServer = puerto

		self.ball = ball
		self.paddle_host = paddle_host
		self.paddle_client = paddle_client
		self.keys = key_states

	def setup_keys(self, wn):
		self.wn = wn
		self.wn.listen()
		for key in self.keys:
			self.wn.onkeypress(lambda k=key: self.keys.update({k: True}), key)
			self.wn.onkeyrelease(lambda k=key: self.keys.update({k: False}), key)

	def iniciar(self):   
		serverSocketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		serverSocketTCP.bind((self.ipServer, self.puertoServer))

		print("***** Servidor TCP iniciado...  ****")
		print("esperando a jugador...")

		serverSocketTCP.listen(1)

		coneccionSocket, direccionIP = serverSocketTCP.accept()
		print(f"Cliente conectado desde {direccionIP}")
		self.jugador_conectado = True
		try:
			while True:
				datos = f"paddle_host|{self.paddle_host.ycor()}|ball|{self.ball.xcor()}|{self.ball.ycor()}"
				coneccionSocket.send(datos.encode())

				datos_client = coneccionSocket.recv(1024).decode()
				tipo, pos = datos_client.split('|')

				self.paddle_client.sety(float(pos))

		except Exception as e:
			print(e)

		finally:
			if coneccionSocket:
				coneccionSocket.close()
			serverSocketTCP.close()
	
	def mover_paddles(self):
		if self.keys.get("w") and self.paddle_host.ycor() < 250:
			self.paddle_host.sety(self.paddle_host.ycor() + 3)
		if self.keys.get("s") and self.paddle_host.ycor() > -250:
			self.paddle_host.sety(self.paddle_host.ycor() - 3)
