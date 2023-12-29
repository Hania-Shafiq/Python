import random
import tkinter as tk
from tkinter import Tk, Label, Entry, Button

numbers = "1234567890"
upper_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower_letters = "qwertyuiopasdfghjklzxcvbnm"
special_characters = "!@#$%^&*()_-+={[}]|:;<,>.?\\/ "

def generate_passwords():
    try:
        n_count = int_var_count.get()
        n_lowerl = int_var_lower.get()
        n_upperl = int_var_upper.get()
        n_numbers = int_var_numbers.get()
        n_special_characters = int_var_special.get()
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid integers.")
        return

    generated_passwords = []
    for _ in range(0, n_count):
        password = ""
        for _ in range(0, n_lowerl):
            chr = random.choice(lower_letters)
            password = chr + password
        for _ in range(0, n_upperl):
            chr = random.choice(upper_letters)
            password = chr + password
        for _ in range(0, n_numbers):
            chr = random.choice(numbers)
            password = chr + password
        for _ in range(0, n_special_characters):
            chr = random.choice(special_characters)
            password = chr + password

        generated_passwords.append(password)

    result_label.config(text="\n".join(generated_passwords))

root = tk.Tk()
root.title("Password Generator")

root.configure(bg="#d3d3d3")

Label(root,text="Welcome to strong password generator",bg="white",fg="black",font="Helvetica 11 bold underline").pack()
Label(root, text="How many passwords do you want?: ", bg="white", fg="black", font="comicsans 9 bold").pack(padx=5, pady=5)
int_var_count = tk.IntVar(value="")  # Initial value is an empty string
entry_count = Entry(root, textvariable=int_var_count)
entry_count.pack()

Label(root, text="How many lowercase letters do you want?: ", bg="white", fg="black", font="comicsans 9 bold").pack(padx=5, pady=5)
int_var_lower = tk.IntVar(value="")  # Initial value is an empty string
entry_lower = Entry(root, textvariable=int_var_lower)
entry_lower.pack()

Label(root, text="How many uppercase letters do you want?: ", bg="white", fg="black", font="comicsans 9 bold").pack(padx=5, pady=5)
int_var_upper = tk.IntVar(value="")  # Initial value is an empty string
entry_upper = Entry(root, textvariable=int_var_upper)
entry_upper.pack()

Label(root, text="How many numbers do you want?: ", bg="white", fg="black", font="comicsans 9 bold").pack(padx=5, pady=5)
int_var_numbers = tk.IntVar(value="")  # Initial value is an empty string
entry_numbers = Entry(root, textvariable=int_var_numbers)
entry_numbers.pack()

Label(root, text="How many symbols do you want?: ", bg="white", fg="black", font="comicsans 9 bold").pack(padx=5, pady=5)
int_var_special = tk.IntVar(value="")  # Initial value is an empty string
entry_special = Entry(root, textvariable=int_var_special)
entry_special.pack()
Button(root, text="Generate-Passwords", command=generate_passwords, bg="white", fg="black", font="comicsans 9 bold").pack(padx=8, pady=8)
result_label = Label(root, text="")
result_label.pack()
root.mainloop()




