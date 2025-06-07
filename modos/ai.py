import random
class PongAi:
    def __init__(self, paddle_player, paddle_ai, ball, key_states):
        self.ball = ball
        self.paddle = paddle_ai
        self.player = paddle_player
        self.keys = key_states
        self.sentido = 1

    def setup_keys(self, wn):
        self.wn = wn
        self.wn.listen()
        for key in self.keys:
            self.wn.onkeypress(lambda k=key: self.keys.update({k: True}), key)
            self.wn.onkeyrelease(lambda k=key: self.keys.update({k: False}), key)

    def mover_paddles(self):
        velocidad = 4
        distancia = random.choice([-340,-100,-200])
        if self.ball.dx > 0 and self.ball.xcor() > distancia:
            prediccion_y = self.predecir_y(self.ball)
            if prediccion_y > self.paddle.ycor() and self.paddle.ycor() < 250:
                self.paddle.sety(self.paddle.ycor() + velocidad)
            elif prediccion_y < self.paddle.ycor() and self.paddle.ycor() > -250:
                self.paddle.sety(self.paddle.ycor() - velocidad)
        else:
            nueva_y = self.paddle.ycor() + (velocidad * self.sentido)
            if nueva_y >= 250:
                nueva_y = 250
                self.sentido = -1 
            elif nueva_y <= -250:
                nueva_y = -250
                self.sentido = 1  

            self.paddle.sety(nueva_y)

        if self.keys.get("w") and self.player.ycor() < 250:
            self.player.sety(self.player.ycor() + 3)
        if self.keys.get("s") and self.player.ycor() > -250:
            self.player.sety(self.player.ycor() - 3)

    def predecir_y(self, ball):
        x, y = ball.xcor(), ball.ycor()
        dx, dy = ball.dx, ball.dy

        while x < 340 and dx > 0:
            x += dx
            y += dy

            if y > 290:
                y = 290
                dy *= -1
            elif y < -290:
                y = -290
                dy *= -1
        return y