import turtle
import winsound
import threading
import time
from datetime import datetime , timedelta #libreraia para: manejra modulos de tiempo, controlar el paso del tiempo


fps = 60 
delay = 1 / fps

wn = turtle.Screen()
wn.title("Pong by @elojosdearroz")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
global score_a ,score_b
score_a = 0
score_b = 0


#KeyBoard Keys
keys = {
    "w": False,
    "s": False,
    "Up": False,
    "Down": False
}


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.speed = 2
ball.dx = 2
ball.dy = 2

#Time
global tiempo_actual, metronome
metronome = 0
tiempo_actual = datetime.strptime("00:00", "%M:%S")

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  00:00  Player B: 0", align="center", font=("Courier", 18, "normal"))

#Function
#Sound
def beep_rebote():
    winsound.Beep(800, 50)

#Movement of ball
def increase_speed():
    # For dx
    if ball.dx > 0:
        ball.dx += 1
    else:
        ball.dx -= 1

    # For dy
    if ball.dy > 0:
        ball.dy += 1
    else:
        ball.dy -= 1

#Movement of paddle_a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
#Movement of paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
#Ketboard binding
# Detectar tecla presionada
def presionar_w():
    keys["w"] = True

def soltar_w():
    keys["w"] = False

def presionar_s():
    keys["s"] = True

def soltar_s():
    keys["s"] = False

def presionar_up():
    keys["Up"] = True

def soltar_up():
    keys["Up"] = False

def presionar_down():
    keys["Down"] = True

def soltar_down():
    keys["Down"] = False

# function to move the ball according to keys
def mover_paletas():
    if keys["w"]:
        y = paddle_a.ycor()
        if y < 250:
            paddle_a.sety(y + 3)
    if keys["s"]:
        y = paddle_a.ycor()
        if y > -250:
            paddle_a.sety(y - 3)
    if keys["Up"]:
        y = paddle_b.ycor()
        if y < 250:
            paddle_b.sety(y + 3)
    if keys["Down"]:
        y = paddle_b.ycor()
        if y > -250:
            paddle_b.sety(y - 3)

wn.listen()
wn.onkeypress(presionar_w, "w")
wn.onkeyrelease(soltar_w, "w")

wn.onkeypress(presionar_s, "s")
wn.onkeyrelease(soltar_s, "s")

wn.onkeypress(presionar_up, "Up")
wn.onkeyrelease(soltar_up, "Up")

wn.onkeypress(presionar_down, "Down")
wn.onkeyrelease(soltar_down, "Down")


#Main game def
def main_game():
    global score_a, score_b, tiempo_actual, metronome
    while True:
        star_time = time.time()
        wn.update()
        mover_paletas()

        #Move the ball
        ball.setx(ball.xcor()+ ball.dx)
        ball.sety(ball.ycor()+ ball.dy)

        #Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            threading.Thread(target=beep_rebote).start()

        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1
            threading.Thread(target=beep_rebote).start()

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            ball.dx = 2
            ball.dy = 2
            metronome = 0
            score_a += 1
            pen.clear()
            pen.write(f"Player A: {score_a}  {tiempo_actual.strftime("%M:%S")}  Player B: {score_b}", align="center", font=("Courier", 18, "normal"))


        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            ball.dx = 2
            ball.dy = 2
            metronome = 0
            score_b += 1
            pen.clear()
            pen.write(f"Player A: {score_a}  {tiempo_actual.strftime("%M:%S")}  Player B: {score_b}", align="center", font=("Courier", 18, "normal"))


        #Paddle and ball colisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
            ball.setx(340)
            ball.dx *= -1
            threading.Thread(target=beep_rebote).start()

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
            ball.setx(-340)
            ball.dx *= -1
            threading.Thread(target=beep_rebote).start()


        elapsed = time.time() - star_time
        time_sleep = delay - elapsed
        #fps management
        if time_sleep > 0:
            time.sleep(time_sleep)
        pen.clear()
        pen.write(f"Player A: {score_a}  {tiempo_actual.strftime("%M:%S")}  Player B: {score_b}", align="center", font=("Courier", 18, "normal"))


#Chronometer contoller
def chronometer():
    global tiempo_actual, metronome
    while True:
        print(tiempo_actual.strftime("%M:%S"))
        tiempo_actual += timedelta(seconds=1)
        time.sleep(1)
        metronome +=1
        if metronome == 5:
            increase_speed()
            metronome = 0
        

threading.Thread(target=chronometer).start()
main_game()
