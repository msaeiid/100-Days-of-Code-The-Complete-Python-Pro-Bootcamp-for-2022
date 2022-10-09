import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game.")
screen.setup(width=725, height=491)
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')


def search_for_state(state_name: str):
    return data[data.state == state_name.title()]


guessed_state = []
while len(guessed_state) < 50:
    user_input = screen.textinput(title=f'{len(guessed_state)}/50 States Correct',
                                  prompt="What's another state's name?")
    result = search_for_state(user_input)
    if user_input.lower() == 'exit':
        # I did before
        missed_states = [state for state in data.state if state not in guessed_state]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('./states_to_learn.csv')
        break
    if len(result):
        temp = turtle.Turtle()
        temp.hideturtle()
        temp.penup()
        temp.goto(int(result.x), int(result.y))
        temp.write(arg=f"{result.state.item()}", move=False)
        screen.update()
        guessed_state.append(result.state.item())

screen.exitonclick()
