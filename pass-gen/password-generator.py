import tkinter as tk
import random
import string

#customizing the GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x600")
root.configure(bg="#1f242a")
label_welcome = tk.Label(root, text="Welcome to Password Generator!", font=30)
label_welcome.pack()

#adding menus
def open_choice():
    l_ask.pack()
    gen_pass.pack_forget()
    exit_b.pack_forget()
    op1.pack()
    op2.pack()
    op3.pack()
    l2_ask.pack()
    slider.pack()
    ok_button.pack()
    back_button.pack()
    password_label.pack()

def go_back():
    l_ask.pack_forget()
    gen_pass.pack()
    exit_b.pack()
    op1.pack_forget()
    op2.pack_forget()
    op3.pack_forget()
    l2_ask.pack_forget()
    slider.pack_forget()
    ok_button.pack_forget()
    back_button.pack_forget()
    password_label.pack_forget()

#checking if these are checked
var_letters = tk.IntVar()
var_numbers = tk.IntVar()
var_symbols = tk.IntVar()

def make_password():
#checks for checkboxes
    password_pool = ""
    if var_letters.get() == 1:
        password_pool += string.ascii_letters
    if var_numbers.get() == 1:
        password_pool += string.digits
    if var_symbols.get() == 1:
        password_pool += string.punctuation
    count = slider.get()
#actually makes password
    if password_pool and count > 0:
        thy_password = random.choices(password_pool, k=count)
        the_pass = ''.join(thy_password)
        password_label.config(text=the_pass)
    elif count == 0:
        S_error = ("Slider set to 0, no password generated.")
        password_label.config(text=S_error)
    else:
        B_error = ("Please select at least one box.")
        password_label.config(text=B_error)

def make_letters():
    print(random.choice(string.ascii_letters))

def make_number():
    print(random.randint(0, 9))

def make_symbol():
    print(random.choice(string.punctuation))

#options
gen_pass = tk.Button(root, text="Generate Password", width=25, command=open_choice)
gen_pass.pack()
exit_b = tk.Button(root, text="Stop", width=25, command=root.destroy)
exit_b.pack()
#options2
l_ask = tk.Label(root, text="How would you want your password to contain?")
op1 = tk.Checkbutton(root, text="Letters", variable=var_letters, width=15, anchor="w")
op2 = tk.Checkbutton(root, text="Numbers", variable=var_numbers, width=15, anchor="w")
op3 = tk.Checkbutton(root, text="Symbols", variable=var_symbols, width=15, anchor="w")
#some buttons and things to interact with
ok_button = tk.Button(root, text="Generate", command=make_password)
back_button = tk.Button(root, text="Go back", command=go_back)
l2_ask = tk.Label(root, text="How long do you want your password to be?")
slider = tk.Scale(root, from_=0, to=20, orient="horizontal")
password_label = tk.Label(root, text="...")

root.mainloop()
