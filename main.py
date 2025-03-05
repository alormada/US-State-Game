import turtle
from state import State
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# alaska = State("alaska", 100, 5)
data = pandas.read_csv("50_states.csv")

score = 0
states = []
for state in data.state:
    states.append(state)

game_on = True
while game_on:
    user_guess = screen.textinput(f"{score}/50 States Correct", "What's another state name?").title()
    if user_guess in states:
        current_state = data[data.state == user_guess]
        x = int(current_state.x)
        y = int(current_state.y)
        correct_answer = State(user_guess, x, y)
        score += 1
    del user_guess


# states = data["state"]
# print(states)

screen.exitonclick()