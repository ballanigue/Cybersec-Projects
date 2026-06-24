import customtkinter as CTK
import random
import string

ascii_cat = r"""
  /\_/\  (
 ( ^.^ ) _)
   \"/  (
 ( | | )
(__d b__)
"""

ascii_cat_s = r"""
    /\_____/\   
   /  O   O  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)
"""

### THINGS TO TAKE NOTE!
# 1. optL = letters
# 2. optN = numbers
# 2. optS = symbols


#customizing window
app = CTK.CTk()
app.geometry("600x700")
CTK.set_appearance_mode("dark")
app.title("Password Cat Generator")

#adding functions
def update_length(value):
    length_num.configure(text=str(int(value)))

# var check
def switch_event():
    print("switch toggled, current value:", optL_switch.get())

def make_password():
#checks for checkboxes
    print("work")

def make_letters():
    print(random.choice(string.ascii_letters))

def make_number():
    print(random.randint(0, 9))

def make_symbol():
    print(random.choice(string.punctuation))

#next the GUI
wlc_label = CTK.CTkLabel(
    app, 
    text="Create Your Password", 
    font=("Arial", 20, "bold"))
wlc_label.pack(pady=20)
the_cat = CTK.CTkLabel(
    master=app,
    text=ascii_cat,
    font=("Consolas", -18),
    justify="left"
)
the_cat.pack()
