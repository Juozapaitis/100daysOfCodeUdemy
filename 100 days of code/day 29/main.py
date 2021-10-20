from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

PATH_TO_IMAGE = "100 days of code//day 29//logo.png"
PATH_TO_DATA = "100 days of code//day 29//data.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_list = []
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    generated_password = "".join(password_list)
    print(generated_password)
    pyperclip.copy(generated_password)
    input_password.delete(0, END)
    input_password.insert(0, generated_password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = input_website.get()
    email_username = input_email_username.get().replace(" ", "")
    password = input_password.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops", message = f"Please don't leave any fields empty!")

    else:
        try:
            with open(PATH_TO_DATA, 'r') as file:
                #Reading old data
                data = json.load(file)
                if website in data:
                    update = messagebox.askyesno(title="Warning", message = f"There is already a password saved for {website}.\n"
                                                                             f"Would you like to overwrite?")
                    if update:
                        data[website]['password'] = password
                        data[website]['email'] = email_username
                    else:
                        return
                else:
                    data.update(new_data)


        except FileNotFoundError:
            with open(PATH_TO_DATA, 'w') as file:
                json.dump(new_data, file, indent = 4)

        else:
            #Updating old data with new data
            data.update(new_data)

            with open(PATH_TO_DATA, 'w') as file:
                #Saving updated data
                json.dump(data, file, indent = 4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)
            input_website.focus_set()

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open(PATH_TO_DATA, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "No data file found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']

            messagebox.showinfo(title = f"{website} password", message = f"Email/Username: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title = "Error", message = f"No details for {website} found")

    # if yes:
    #     messagebox.showinfo(title = f"{website} password", message = f"Website: {website} \nPassword:{pass}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password generator")
window.config(padx = 20, pady = 20)

canvas = Canvas(width = 200, height = 200)
logo_image = PhotoImage(file = PATH_TO_IMAGE)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column = 1, row = 0)

website_label = Label(text = "Website: ", font = ('Arial', 12, 'normal'))
website_label.grid(column = 0, row = 1)
input_website = Entry()
input_website.grid(column = 1, row = 1, sticky = "EW")
input_website.focus_set()


email_username__label = Label(text = "Email/Username: ", font = ('Arial', 12, 'normal'))
email_username__label.grid(column = 0, row = 2)
input_email_username = Entry()
input_email_username.grid(column = 1, row = 2, columnspan = 2, sticky = "EW")
input_email_username.insert(0, 'test@gmail.com')


password_label = Label(text = "Password: ", font = ('Arial', 12, 'normal'))
password_label.grid(column = 0, row = 3)
input_password = Entry()
input_password.grid(column = 1, row = 3, sticky = "EW")

search_button = Button(text = "Search", command = find_password)
search_button.grid(column = 2, row = 1, sticky = "EW")

generate_password_button = Button(text = "Generate Password", command = generate_password)
generate_password_button.grid(column = 2, row = 3, sticky = "EW")

add_button = Button(text = "Add", width = 36, command = save_password)
add_button.grid(column = 1, row = 4, columnspan = 2, sticky = "EW")

window.mainloop()