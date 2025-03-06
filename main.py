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

data_dict = {}
guessed_states = []
guessed_x = []
guessed_y = []
game_on = True
while game_on:
    user_guess = screen.textinput(f"{score}/50 States Correct", "What's another state name?").title()
    if user_guess in states:
        current_state = data[data.state == user_guess]
        x = int(current_state.x)
        y = int(current_state.y)
        correct_answer = State(user_guess, x, y)
        score += 1
        guessed_states.append(user_guess)
        guessed_x.append(x)
        guessed_y.append(y)
    elif user_guess == "Exit":
        game_on = False

for guess in guessed_states:
    data_dict["state"] = guessed_states
    data_dict["x"] = guessed_x
    data_dict["y"] = guessed_y

df = pandas.DataFrame(data_dict)
df.to_csv("current_progress.csv")

screen.exitonclick()