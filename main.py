import turtle
from turtle import Screen, Turtle
import pandas

ALIGN = "center"
FONT=("Arial", 12, "normal")

states_data = pandas.read_csv('50_states.csv')
states = states_data['state']
correct = 0
total = len(states)
is_on = True

screen = Screen()
pic = Turtle()
pen = Turtle()
pen.hideturtle()
pen.penup()

screen.title('US States Game')
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

while is_on:
    user_input = screen.textinput(title=f'{correct} / {total} States Correct', prompt="What's another state's name?").title()
    if user_input in states.tolist():
        correct += 1
        x_coord = states_data[states_data.state == user_input].x.to_list()
        y_coord = states_data[states_data.state == user_input].y.to_list()
        pen.goto(x=x_coord[0], y=y_coord[0])
        pen.write(user_input, align=ALIGN, font=FONT)
    else:
        continue

screen.exitonclick()

