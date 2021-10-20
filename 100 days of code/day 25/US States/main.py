import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "100 days of code//day 25//US States//blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("100 days of code//day 25//US States//50_states.csv")
all_states = data.state.to_list()
# print(data["y"])
# print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", 
                                    prompt = "What's another state's name?").title()
    
    if answer_state == "Exit":
        states_left = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(states_left, columns = ['state'])
        df.to_csv("100 days of code\\day 25\\US States\\states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

        guessed_states.append(answer_state)

    elif answer_state in guessed_states:
        print("You already guessed this state")

# If guessed all
if len(guessed_states) == 50:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("red")
    t.goto(-150, 250)
    t.write("You win!", font = ('Arial', 48, 'normal', 'bold'))
    
    # screen.mainloop()
#     xcor = data["x"]
#     xc = xcor.to_string(index = False)

#     ycor = data["y"]
#     yc = ycor.to_string(index = False)

#     print("Yes")
#     turtle.penup()
#     turtle.goto(xc, yc)
#     turtle.write(answer_state, align = "center")
