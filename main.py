from turtle import Turtle, Screen
from random import choice, randint
import time


def draw_lines():
    text, line = Turtle(), Turtle()
    text.ht(), text.pu(), text.color(227, 190, 83), text.goto(x=0, y=160)
    text.write("The Grand Turtle Race", font=("Arial", 20, "bold"), align="center")
    text.color(227, 70, 83), text.goto(x=-280, y=157)
    text.write("Start", font=("Arial", 17, "bold"), align="center")
    text.color(141, 180, 84), text.goto(x=280, y=157)
    text.write("Finish", font=("Arial", 17, "bold"), align="center")
    line.ht(), line.pu(), line.width(5), line.seth(90), line.goto(x=-280, y=-150), line.pd()
    for _ in range(10):
        line.color(113, 155, 208)
        line.fd(15)
        line.color(230, 155, 127)
        line.fd(15)
    line.speed("fast"), line.pu(), line.goto(x=280, y=-150), line.speed("slow"), line.pd()
    for _ in range(10):
        line.color(113, 155, 208)
        line.fd(15)
        line.color(230, 155, 127)
        line.fd(15)
    line.width(2), line.pu(), line.seth(0), line.speed("normal"), line.color("white")
    vertical = -140
    for _ in range(8):
        line.goto(x=-290, y=vertical)
        vertical += 40
        line.pd()
        line.fd(600)
        line.pu()


screen = Screen()
screen.setup(width=700, height=400)
screen.bgcolor("black")
screen.title("The Grand Turtle Race")
screen.colormode(255)
draw_lines()

betters = []
no_of_betters = int(screen.numinput("The Grand Turtle Race!!!", "How many players want to place bets?"))
for i in range(no_of_betters):
    user_input = screen.textinput("Make your bet", "Enter your name and "
                                                   "bet on the turtle you think will win the race?").split(", ")
    betters.append((user_input[0].title(), user_input[1].lower()))

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
y = -120

for i in range(7):
    cur_turtle = Turtle()
    cur_turtle.color(colors[i])
    cur_turtle.shape("turtle")
    cur_turtle.pu()
    cur_turtle.goto(-300, y)
    y += 40
    turtles.append(cur_turtle)

timer = Turtle()
timer.ht()
colors = ["green", "yellow", "red"]
for sec in range(3, 0, -1):
    timer.color(colors[sec - 1])
    timer.write(sec, font=("Arial", 30, "bold"))
    time.sleep(1)
    timer.clear()
race_in_progress = True
winner = ""

while race_in_progress:
    moving_turtle = choice(turtles)
    # if moving_turtle.color()[0] == "blue":
    #     steps = 10
    # elif moving_turtle.color()[0] == "yellow":
    #     steps = 0
    # else:
    steps = randint(0, 10)
    moving_turtle.fd(steps)
    for turtle in turtles:
        if turtle.xcor() > 270:
            race_in_progress = False
            winner = turtle.pencolor()

did_anyone_win = False
for bet in betters:
    if winner == bet[1]:
        print(f"{bet[0]} wins. The {winner} turtle won the race.")
        did_anyone_win = True

if not did_anyone_win:
    print(f"Everyone loses. The {winner} turtle won the race.")

win_screen = Screen()

screen.exitonclick()
