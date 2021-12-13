import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Guess the State", prompt="What´s another state name?")
print(answer)

df = pandas.read_csv("50_states.csv")
print(df)
# def get_mouse(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse)
# turtle.mainloop()

#screen.exitonclick()