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

#decorating slider
slider_frame = CTK.CTkFrame(
    master=app,
    corner_radius=12
)
slider_frame.pack(fill="x", padx=20, pady=(10, 20))

length_label = CTK.CTkLabel(
    master=slider_frame,
    text="LENGTH:",
    text_color="#A0A5AA",
    font=("Arial", 11, "bold")
)
length_label.grid(row=0, column=0, sticky="w", padx=(15, 0), pady=(10, 0))
length_num = CTK.CTkLabel(
    master=slider_frame,
    text="0",
    font=("Arial", 11, "bold")
)
length_num.grid(row=0, column=1, columnspan=2, sticky="w", padx=(5, 0), pady=(10, 0))
min_label = CTK.CTkLabel(
    master=slider_frame,
    text="0",
    font=("Arial", 13, "bold")
)

min_label.grid(row=1, column=0, padx=(15, 5), pady=(5, 15))
slider = CTK.CTkSlider(
    master=slider_frame,
    number_of_steps=60, 
    from_=0, 
    to=20, 
    command=update_length)
slider.grid(row=1, column=1, sticky="ew", pady=(5, 15))
slider.set(0)
max_label = CTK.CTkLabel(
    master=slider_frame,
    text="20",
    font=("Arial", 13, "bold")
)
max_label.grid(row=1, column=2, padx=(5, 15), pady=(5, 15))
slider_frame.grid_columnconfigure(1, weight=1)

#the options
opt_frame = CTK.CTkFrame(
    master=app,
    corner_radius=12
)
opt_frame.pack(fill="x", padx=20, pady=(10, 20))
opt_frame.grid_columnconfigure(0, weight=1)
opt_label = CTK.CTkLabel(
    master=opt_frame,
    text="OPTIONS",
    text_color="#A0A5AA",
    font=("Arial", 11, "bold")
)
opt_label.grid(row=0, column=0, sticky="w", padx=(15, 0), pady=(10, 0))
