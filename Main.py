from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(4, 6)
    nr_numbers = random.randint(2, 4)

    password_list = []
    symbol_list = []
    letter_list=[]

    letter_list= [random.choice(letters) for char in range(nr_letters) ]
    symbol_list= [random.choice(symbols) for char in range(nr_symbols) ]
    password_list= [random.choice(numbers) for char in range(nr_numbers) ]

    password_list += letter_list + symbol_list
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    websitename= website_input.get()
    email= username_input.get()
    password= password_input.get()
    new_dict={
        websitename:{"email" : email, "password": password
    }
    }
    if len(websitename) == 0 or len(password) == 0:
        messagebox.showerror("Error", message="Please enter data in every field")
    else:
        is_ok= messagebox.askokcancel(title="Warning", message=f"website name:{websitename}, username:{email}, password= {password} \n should i save this data?")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_dict, data_file, indent=4)
            else:
                data.update(new_dict)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0,END)
                password_input.delete(0,END)


def find_password():
    website= website_input.get().lower()
    email = username_input.get().lower()
    try:
        with open("data.json") as data_file:
            data= json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo( title="Error", message="No data found" )
    else:
        if website and email in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo ( title=website, message=f"Email \ Website:{email}\n Password:{password}" )
        else:
            messagebox.showinfo ( title="Error", message="No data found" )

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
canvas = Canvas(width= 200, height= 200)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0,"")

password_input = Entry(width =21)
password_input.grid(column=1, row=3)

search_button = Button(text="Search", width =15, command= find_password)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command= pass_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text= "ADD", width=36, command= save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
