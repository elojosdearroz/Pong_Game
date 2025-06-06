# main.py
import threading
import turtle
from ui.interfaz import InterfazPong
from ui.controlador import ControladorJuego
from modos.offline import PongOffline
from modos.ai import PongAi

keys = {"w": False, "s": False, "Up": False, "Down": False}

def crear_paddle(x_pos):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.penup()
    paddle.goto(x_pos, 0)
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    return paddle

def crear_pelota():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = 2
    return ball

def modo_offline():
    paddle_a = crear_paddle(-350)
    paddle_b = crear_paddle(350)
    ball = crear_pelota()
    juegoOffline = PongOffline(paddle_a, paddle_b, keys)
    juegoOffline.setup_keys(wn)
    juego = ControladorJuego(wn, paddle_a, paddle_b, ball, juegoOffline)
    juego.iniciar()

def modo_ai():
    paddle_a = crear_paddle(-350)
    paddle_b = crear_paddle(350)
    ball = crear_pelota()
    juegoai = PongAi(paddle_a, paddle_b, ball, keys)
    juegoai.setup_keys(wn)
    juego = ControladorJuego(wn, paddle_a, paddle_b, ball, juegoai)
    juego.iniciar()


def modo_online():
    print("Modo online no implementado aun.")

# Crear pantalla
wn = turtle.Screen()
wn.title("Pong by @elojosdearroz")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Lanzar menú principal
interfaz = InterfazPong()
interfaz.wn = wn
interfaz.mostrar_menu({
    "offline": modo_offline,
    "ai": modo_ai,
    "online": modo_online
})
interfaz.iniciar_loop()
