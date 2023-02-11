import turtle
import pandas
import sys

screen = turtle.Screen()
screen.title('US quiz game')
obiect = turtle.Turtle()
screen.addshape('blank_states_img.gif')
obiect.shape('blank_states_img.gif')

file = pandas.read_csv('50_states.csv')
data_file = pandas.DataFrame(file)
len_state = len(data_file.state)
# print(data_file.state.to_list())
count = 0
list_temp = []
while len(list_temp) < len_state:
    answer = turtle.textinput(title=f'{count}/{len_state} State corecte', prompt='Scrie un stat in casuta').title()
    find_data = data_file[data_file.state == answer]
    state = find_data.state.to_list()
    if answer == 'Exit':
        data_dict = {}
        data_dict['state'] = list_temp
        new_data = pandas.DataFrame(data_dict)
        new_data.to_csv('states_to_learn.csv')
        sys.exit()

    if answer in data_file.state.to_list() and answer not in list_temp:
        list_temp.append(answer)
        x_cor = int(find_data.x)
        y_cor = int(find_data.y)
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(x=x_cor, y=y_cor)
        turtle.write(arg=state[0])
        count += 1


screen.mainloop()
