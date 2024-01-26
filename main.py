import turtle
import pandas

screen = turtle.Screen()
screen.title("Japan Prefecture Game")
image = "blank_japan_prefs.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

with open("japan_prefecture_coordinates.csv") as file:
    data = pandas.read_csv(file)
    prefectures = data.prefecture.to_list()

guessed_prefectures = []

while len(guessed_prefectures) < 47:
    answer_prefecture = screen.textinput(title=f"{len(guessed_prefectures)}/47 Prefectures Correct", prompt="What's another prefecture's name?").title()
    if answer_prefecture == "Exit": #this
        missing_prefectures = [prefectures for prefectures in prefectures if prefectures not in guessed_prefectures]
        new_data = pandas.DataFrame(missing_prefectures)
        new_data.to_csv("prefectures_to_learn.csv")


        break
    if answer_prefecture in prefectures:
        guessed_prefectures.append(answer_prefecture)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        prefecture_data = data[data.prefecture == answer_prefecture]
        t.goto(int(prefecture_data.x), int(prefecture_data.y))
        t.write(answer_prefecture)

turtle.mainloop()





#screen.exitonclick()