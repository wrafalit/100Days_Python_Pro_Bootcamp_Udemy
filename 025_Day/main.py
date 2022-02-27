import turtle
import pandas

data = pandas.read_csv("50_states.csv")

# list of states
states50 = data["state"].tolist()


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# state = data[data["state"] == "Arizona"]
# x = state.x
# print(int(x))


count = 0
answer_list = []
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{count}/50 States Correct", prompt="what's another state's name?").title()

    if answer_state == "Exit":
        new_list = [state for state in states50 if state not in answer_list]
        states_to_learn = pandas.DataFrame(new_list)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if answer_state in states50:
        if answer_state not in answer_list:
            t = turtle.Turtle()
            t.hideturtle()
            index = states50.index(answer_state)
            answer_list.append(answer_state)
            count +=1
            state_cor = data[data["state"] == answer_state].to_dict()
            x = state_cor['x'][index]
            y = state_cor['y'][index]
            t.pu()
            t.goto(x, y)
            t.write(answer_state,False)
    if count == 49:
        game_on = False








# def get_mouse_click_coor(x,y):
#     print((x,y))
#
# turtle.onscreenclick(get_mouse_click_coor)
# screen.mainloop()




# screen.exitonclick()