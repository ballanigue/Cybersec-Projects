import tkinter as tk
import random

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
    back_button.pack()

def go_back():
    l_ask.pack_forget()
    gen_pass.pack()
    exit_b.pack()
    op1.pack_forget()
    op2.pack_forget()
    op3.pack_forget()
    back_button.pack_forget()

def make_password():
    print(random.randint(0, 9))

#options
gen_pass = tk.Button(root, text="Generate Password", width=25, command=open_choice)
gen_pass.pack()
exit_b = tk.Button(root, text="Stop", width=25, command=root.destroy)
exit_b.pack()
#options2
l_ask = tk.Label(root, text="How would you want your password to contain?")
op1 = tk.Checkbutton(root, text="Letters", variable=1, width=15, anchor="w")
op2 = tk.Checkbutton(root, text="Numbers", variable=2, width=15, anchor="w")
op3 = tk.Checkbutton(root, text="Symbols", variable=3, width=15, anchor="w")
ok_button = tk.Checkbutton(root, text="Generate", variable=4, width=15, anchor="w", command=make_password)
back_button = tk.Button(root, text="Go back", command=go_back)

root.mainloop()
