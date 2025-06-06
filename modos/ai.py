class PongAi:
    def __init__(self, paddle_player, paddle_ai, ball, key_states):
        self.ball = ball
        self.paddle = paddle_ai
        self.player = paddle_player
        self.keys = key_states

    def setup_keys(self, wn):
        self.wn = wn
        self.wn.listen()
        for key in self.keys:
            self.wn.onkeypress(lambda k=key: self.keys.update({k: True}), key)
            self.wn.onkeyrelease(lambda k=key: self.keys.update({k: False}), key)

    def mover_paddles(self):
        velocidad = 4
        if self.ball.ycor()  > self.paddle.ycor():
            self.paddle.sety(self.paddle.ycor() + velocidad)
        elif self.ball.ycor()  < self.paddle.ycor():
            self.paddle.sety(self.paddle.ycor() - velocidad)

        if self.keys.get("w") and self.player.ycor() < 250:
            self.player.sety(self.player.ycor() + 3)
        if self.keys.get("s") and self.player.ycor() > -250:
            self.player.sety(self.player.ycor() - 3)

