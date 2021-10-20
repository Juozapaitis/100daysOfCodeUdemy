from tkinter import *

def convert():
    miles_to_km = float(input.get()) * 1.609
    my_label_1.config(text = round(miles_to_km))

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)
window.minsize(width = 300, height = 100)


input = Entry(width = 10)
input.grid(column = 1, row = 0)

my_label = Label(text = "Miles", font = ("Arial", 12, 'bold'))
my_label.grid(column = 2, row = 0)

my_label = Label(text = "is equal to ", font = ("Arial", 12, 'bold'))
my_label.grid(column = 0, row = 1)

my_label_1 = Label(text = "0")
my_label_1.grid(column = 1, row = 1)

my_label = Label(text = "Km", font = ("Arial", 12, 'bold'))
my_label.grid(column = 2, row = 1)

button = Button(text = "Convert", command = convert)
button.grid(column = 1, row = 2)





window.mainloop()