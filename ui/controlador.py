import turtle
import winsound
import threading
import time
from datetime import datetime, timedelta

fps = 60
delay = 1 / fps

class ControladorJuego:
    def __init__(self, wn, paddle_a, paddle_b, ball, controlador_paddles):
        self.wn = wn
        self.paddle_a = paddle_a
        self.paddle_b = paddle_b
        self.ball = ball
        self.controlador_paddles = controlador_paddles

        self.score_a = 0
        self.score_b = 0
        self.metronome = 0
        self.current_time = datetime.strptime("00:00", "%M:%S")

        # Score display
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self._update_scoreboard()

    def _update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"Player A: {self.score_a}  {self.current_time.strftime('%M:%S')}  Player B: {self.score_b}",
                       align="center", font=("Courier", 18, "normal"))

    def _play_bounce_sound(self):
        winsound.Beep(800, 50)

    def _play_lose_sound(self):
        winsound.Beep(300, 50)

    def _increase_speed(self):
        self.ball.dx += 1 if self.ball.dx > 0 else -1
        self.ball.dy += 1 if self.ball.dy > 0 else -1

    def iniciar(self):
        if hasattr(self.controlador_paddles, "iniciar"):
            threading.Thread(target=self.controlador_paddles.iniciar, daemon=True).start()

        if hasattr(self.controlador_paddles, "jugador_conectado" ):
            while not self.controlador_paddles.jugador_conectado:
                time.sleep(1)
                print("esperando jugador....")
    
        threading.Thread(target=self._cronometro, daemon=True).start()
        self._game_loop()

    def _game_loop(self):
        while True:
            start_time = time.time()
            self.wn.update()
            self.controlador_paddles.mover_paddles()

            # Movimiento de la pelota
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Colisiones con bordes
            if self.ball.ycor() > 290:
                self.ball.sety(290)
                self.ball.dy *= -1
                threading.Thread(target=self._play_bounce_sound).start()

            if self.ball.ycor() < -280:
                self.ball.sety(-280)
                self.ball.dy *= -1
                threading.Thread(target=self._play_bounce_sound).start()

            # Puntos
            if self.ball.xcor() > 390:
                self._reset_ball()
                self.score_a += 1
                threading.Thread(target=self._play_lose_sound).start()

            if self.ball.xcor() < -390:
                self._reset_ball()
                self.score_b += 1
                threading.Thread(target=self._play_lose_sound).start()

            # Colisiones con paddles
            if (340 < self.ball.xcor() < 350) and (self.paddle_b.ycor() - 50 < self.ball.ycor() < self.paddle_b.ycor() + 50):
                self.ball.setx(340)
                self.ball.dx *= -1
                threading.Thread(target=self._play_bounce_sound).start()

            if (-350 < self.ball.xcor() < -340) and (self.paddle_a.ycor() - 50 < self.ball.ycor() < self.paddle_a.ycor() + 50):
                self.ball.setx(-340)
                self.ball.dx *= -1
                threading.Thread(target=self._play_bounce_sound).start()

            # Control de FPS
            elapsed = time.time() - start_time
            sleep_time = delay - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)

            self._update_scoreboard()

    def _reset_ball(self):
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = 2
        self.metronome = 0

    def _cronometro(self):
        while True:
            time.sleep(1)
            self.current_time += timedelta(seconds=1)
            self.metronome += 1
            if self.metronome == 5:
                self._increase_speed()
                self.metronome = 0
