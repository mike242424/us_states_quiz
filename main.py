import turtle
from turtle import Screen, Turtle
import pandas

ALIGN = "center"
FONT = ("Arial", 12, "normal")

states_data = pandas.read_csv('50_states.csv')
states = states_data['state'].to_list()
guessed_states = []
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
    user_input = screen.textinput(title=f'{correct} / {total} '
                                        f'States Correct', prompt="What's another state's name?").title()

    if user_input == 'Exit':
        is_on = False
    if user_input in states:
        correct += 1
        guessed_states.append(user_input)
        if correct == total:
            is_on = False
        x_coord = states_data[states_data.state == user_input].x.iloc[0]
        y_coord = states_data[states_data.state == user_input].y.iloc[0]
        pen.goto(x=x_coord, y=y_coord)
        pen.write(user_input, align=ALIGN, font=FONT)
    else:
        continue

not_guessed_states = [states for states in states if states not in guessed_states]
pandas.DataFrame(not_guessed_states).to_csv('missed_states.csv')
