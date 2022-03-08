import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice((letters)) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice((symbols)) for _ in range(random.randint(2, 4))]
    password_number = [random.choice((numbers)) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_number + password_symbol
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    saved_password = f"{web_entry.get()} | {email_username_entry.get()} | {password_entry.get()}\n"
    # print(len(web_entry.get()) ," ", len(password_entry.get()))
    website = web_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email": email,
            "password": password,
        }
    }
    if len(web_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Opss", message="Pleaase don't leave any field empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", mode="w") as data_file:
                # write
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # write
                json.dump(data, data_file, indent=4)
        finally:
                delete()


def delete():
    web_entry.delete(0, END)
    password_entry.delete(0, END)

# ----------------------------  SEARCH  ------------------------------- #
def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="opss", message="No Data file found!")
    else:

        website = web_entry.get()
        search_email = data[website]['email']
        search_password = data[website]['password']

        for d in data:
            if d == website:
                messagebox.showinfo(title=website, message=f"Email: {search_email}\n"
                                                      f"Password: {search_password}")
            else:
                messagebox.showinfo(title="website no exist", message="No details for the website exist")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=20)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1)
web_entry.get()

email_username_entry = Entry(width=35)
email_username_entry.insert(END, "email@ww.ww")
email_username_entry.grid(column=1, row=2)
email_username_entry.get()

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)
password_entry.get()

# Button
generate_button = Button(text="Generate Password", width=20, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

add_search = Button(text="Search", width=20, command=find_password)
add_search.grid(column=2, row=1)

window.mainloop()
