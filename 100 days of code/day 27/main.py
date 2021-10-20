from tkinter import *

def button_clicked():
    print("I got clicked! ")
    new_text = input.get()
    my_label.config(text = new_text)

window = Tk()
window.title("First GUI Program")
window.minsize(width = 500, height = 300)

# Label

my_label = Label(text = "Enter a label", font = ("Arial", 24, 'bold'))
my_label.pack()

# my_label["text"] = "New Text"
# my_label.config(text = "New Text")

# Entry

input = Entry(width = 10)
input.pack()

button = Button(text = "Click me", command = button_clicked)
button.pack()

window.mainloop()

# def add(*args):
#     return sum(args)

# print(add(1, 2, 3))

# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add=3, multiply=5)

# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.color = kwargs.get("color")


# my_car = Car(make="Nissan", model = "GTR")
# print(my_car.make)