from pathlib import Path
import turtle as t
import pandas as pd

from writer import Writer

BASE_DIR = Path(__file__).parent
screen = t.Screen()
screen.title("U.S. States Quiz")
background_path = str(BASE_DIR / "blank_states_img.gif")
screen.addshape(background_path)
t.shape(background_path)
writer = Writer()
df = pd.read_csv(BASE_DIR / "50_states.csv")


states_guessed = []

while len(states_guessed) < 50:
    user_answer = screen.textinput(
        title=f"{len(states_guessed)}/50 states guessed", prompt="Write state's name:"
    ).title()

    if user_answer == "Exit":
        break

    if user_answer in df.state.values and user_answer not in states_guessed:
        state = user_answer.title()
        x = df[df.state == state].x.item()
        y = df[df.state == state].y.item()
        writer.display_state(state, x, y)
        states_guessed.append(state)

result_dict = {"State": [], "Guessed": []}

for state in df.state.values:
    result_dict["State"].append(state)
    if state not in states_guessed:
        result_dict["Guessed"].append(False)
    else:
        result_dict["Guessed"].append(True)

new_df = pd.DataFrame(result_dict)
new_df.to_csv(BASE_DIR / "results.csv")
