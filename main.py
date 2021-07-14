import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.states.to_list()

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
missing_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Enter the name here :").title()

    if answer_state == 'Exit':
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("Yet_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.ht()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f'{answer_state}')
        guessed_states.append(answer_state)

screen.exitonclick()
