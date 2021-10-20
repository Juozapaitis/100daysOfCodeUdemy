import pandas
import turtle
import unidecode

screen = turtle.Screen()
screen.title("Lietuvos miestų žaidimas")
screen.setup(width=0.99, height=0.99, startx=0, starty=0)

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

image = "100 days of code//day 25//lietuvos miestai//lietuvos-žemėlapis-vektorius.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("100 days of code//day 25//lietuvos miestai//50_lietuvos_miestu_pagal_populiacija.csv")
all_cities = data.city.to_list()
# print(data["y"])
# print(all_cities)
guessed_cities = []

while len(guessed_cities) < 50:
    # def get_mouse_click_coor(x, y):
    #     print(x, y)

    # turtle.onscreenclick(get_mouse_click_coor)

    # turtle.mainloop()

    answer_city = screen.textinput(title = f"{len(guessed_cities)}/50 miestų su didžiausia populiacija", 
                                    prompt = "Norint išeiti įveskite 'Baigiau'. Miesto pavadinimas:").title()
    unidecode.unidecode(answer_city)
    if answer_city == "Baigiau":
        cities_left = []
        for city in all_cities:
            if city not in guessed_cities:
                cities_left.append(city)
        df = pandas.DataFrame(cities_left, columns = ['city'])
        df.to_csv("100 days of code//day 25//lietuvos miestai//likę_miestai.csv")
        break
    if answer_city in all_cities and answer_city not in guessed_cities:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data = data[data.city == answer_city]
        print(city_data.x)
        t.goto(int(city_data.x), int(city_data.y))
        t.color("black")
        t.write(answer_city, font = ('Arial', 12, 'normal', 'bold'))

        guessed_cities.append(answer_city)
    
        

# If guessed all
if len(guessed_cities) == 50:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("red")
    t.goto(-150, 250)
    t.write("Atspėjote visus", font = ('Arial', 48, 'normal', 'bold'))
    
    # screen.mainloop()
#     xcor = data["x"]
#     xc = xcor.to_string(index = False)

#     ycor = data["y"]
#     yc = ycor.to_string(index = False)

#     print("Yes")
#     turtle.penup()
#     turtle.goto(xc, yc)
#     turtle.write(answer_city, align = "center")

# screen.exitonclick()