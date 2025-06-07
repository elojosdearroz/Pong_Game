# interfaz.py

import turtle

class InterfazPong:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Pong by @elojosdearroz")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

        self.buttonA = turtle.Turtle()
        self.buttonB = turtle.Turtle()
        self.buttonC = turtle.Turtle()

        self.button_server = turtle.Turtle()
        self.button_client = turtle.Turtle()

    def mostrar_menu(self, callbacks):
        self._dibujar_boton(self.buttonA, 0, 100, "JUGADOR VS. JUGADOR")
        self._dibujar_boton(self.buttonB, 0, 0, "JUGADOR VS. A.I.")
        self._dibujar_boton(self.buttonC, 0, -100, "JUGADOR VS. JUGADOR ONLINE")

        self.buttonA.onclick(lambda x, y: self._accion(callbacks.get('offline')))
        self.buttonB.onclick(lambda x, y: self._accion(callbacks.get('ai')))
        self.buttonC.onclick(lambda x, y: self._accion(callbacks.get('online')))
        self.wn.update()

    def mostrar_menuOnline(self, callbacks):
        self._dibujar_boton(self.button_server, 0, 100, "CREAR PARTIDA")
        self._dibujar_boton(self.button_client, 0, 0, "UNIRESE A PARTIDA")

        self.button_server.onclick(lambda x, y: self._accion(callbacks.get('server')))
        self.button_client.onclick(lambda x, y: self._accion(callbacks.get('client')))
        self.wn.update()
    
    
    def _dibujar_boton(self, boton, x, y, mensaje):
        boton.pencolor("#FFFFFF")
        boton.fillcolor("")
        boton.shape("square")
        boton.penup()
        boton.goto(x, y)
        boton.shapesize(stretch_wid=3, stretch_len=15)
        boton.write(mensaje, align="center", font=("Courier", 10, "bold"))

    def _accion(self, callback):
        self.eliminar_botones()
        if callback:
            callback()

    def eliminar_botones(self):
        for boton in (self.buttonA, self.buttonB, self.buttonC, self.button_server, self.button_client):
            boton.clear()
            boton.hideturtle()
        self.wn.update()

    def iniciar_loop(self):
        turtle.done()
