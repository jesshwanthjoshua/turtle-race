from turtle import Turtle, Screen
from random import randint

race_on = False

screen_3 = Screen()
screen_3.setup(width=540, height=400)
user_input = screen_3.textinput(title="Place your bet.", prompt="Guess the color of the winning turtle.")
print(f"user_input: {user_input}\n\n")

"""turtle race"""
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtles = []
x = -250
y = -90

for n in range(len(colors)):
    mike = Turtle(shape="turtle")
    mike.color(colors[n])
    mike.penup()
    mike.setpos(x, y)
    turtles.append(mike)
    # print(mike.position())
    y += 30

if user_input:
    race_on = True
    print("\n\n")

while race_on:
    for turtle in turtles:
        turtle.forward(randint(1, 10))
        # print(f"{turtle.pencolor()}: {turtle.position()}")

        if turtle.xcor() > 250:
            race_on = False
            if turtle.color() == user_input:
                print(f"You Win. The {turtle.color()} turtle is the winner.")
            else:
                print(f"You Lose. The {turtle.color()} turtle is the winner.")
            break

screen_3.exitonclick()
