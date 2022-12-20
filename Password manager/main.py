from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)
    # Python String Join() method
    password = "".join(password_list)
    # print(f"You password is: {password}")
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as access_file:
                data = json.load(access_file)
                show_data = data[website]
                messagebox.showinfo(title=website, message=f"Email: {show_data['email']}"
                                                           f"\nPassword: {show_data['password']}")
        except FileNotFoundError:
            messagebox.showwarning(title="Information", message=f"No Data File Found.")
        except KeyError:  # I can also use If and Else in this Situation
            messagebox.showerror(title="Oops", message=f"No details for the {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "password": password,
            "email": email
        }
    }
    # print(f"{password_name}|{website_name}|{email_name}")
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Is Save?", message=f"These are the details entered:\nEmail: {email} "
                                                                 f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # take json file format and convert as a dictionary
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="password:")
website_label.grid(column=0, row=1)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=60)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@email.com")
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, command=find_password)
gen_password_button = Button(text="Generate Password", width=15, command=generate_password)
add_button = Button(text="Add", width=50, command=save)
gen_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)

window.mainloop()
