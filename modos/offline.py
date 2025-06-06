class PongOffline:
    def __init__(self, paddle_a, paddle_b, key_states):
        self.paddle_a = paddle_a
        self.paddle_b = paddle_b
        self.keys = key_states

    def setup_keys(self, wn):
        self.wn = wn
        self.wn.listen()
        for key in self.keys:
            self.wn.onkeypress(lambda k=key: self.keys.update({k: True}), key)
            self.wn.onkeyrelease(lambda k=key: self.keys.update({k: False}), key)

    def mover_paddles(self):
        if self.keys.get("w") and self.paddle_a.ycor() < 250:
            self.paddle_a.sety(self.paddle_a.ycor() + 3)
        if self.keys.get("s") and self.paddle_a.ycor() > -250:
            self.paddle_a.sety(self.paddle_a.ycor() - 3)

        if self.keys.get("Up") and self.paddle_b.ycor() < 250:
            self.paddle_b.sety(self.paddle_b.ycor() + 3)
        if self.keys.get("Down") and self.paddle_b.ycor() > -250:
            self.paddle_b.sety(self.paddle_b.ycor() - 3)
