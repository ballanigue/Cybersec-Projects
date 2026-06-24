import customtkinter as CTK
import random
import string

ascii_cat = r"""
              /\_____/\ 
             /  -   -  \  not
            ( ==  ^  == )   looking..
             )         (
            (           )
           ( (  )   (  ) )
          (__(__)___(__)__)
"""

ascii_cat_s = r"""
       /\_____/\   
      /  O   O  \ ! ! !
     ( ==  ^  == )
      )         (
     (           )
    ( (  )   (  ) )
   (__(__)___(__)__)
"""

ascii_cat_o = r"""
    /\_____/\ 
   /  .   .  \
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

def gen_menu():
    #the CAT!
    the_Ccat.pack()
    the_ocat.pack_forget()
    the_Scat.pack_forget()
    #Show Slider & options
    slider_frame.pack(fill="x", padx=20, pady=(10, 20))
    opt_frame.pack(fill="x", padx=20, pady=(10, 20))
    #Show
    make_btn.pack(padx=10, pady=5)
    back_btn.pack(padx=10, pady=5)
    copy_plabel.pack(padx=10, pady=5)
    #Forget
    start_btn.pack_forget()
    stngs_btn.pack_forget()
    quit_btn.pack_forget()

def go_back():
    #the CAT!
    the_Ccat.pack_forget()
    the_ocat.pack()
    #Show
    start_btn.pack(padx=10, pady=5)
    stngs_btn.pack(padx=10, pady=5)
    quit_btn.pack(padx=10, pady=5)
    #Forget
    slider_frame.pack_forget()
    opt_frame.pack_forget()
    make_btn.pack_forget()
    back_btn.pack_forget()
    copy_plabel.pack_forget()

def update_length(value):
    length_num.configure(text=str(int(value)))

#vars
optL_var = CTK.StringVar(value="off")
optN_var = CTK.StringVar(value="off")
optS_var = CTK.StringVar(value="off")

def make_password():
#checks for switches
    password_pool = ""
    if optL_var.get() == "on":
        password_pool += string.ascii_letters
    if optN_var.get() == "on":
        password_pool += string.digits
    if optS_var.get() == "on":
        password_pool += string.punctuation
    count = int(slider.get())
    copy_plabel.configure(state="normal")
    copy_plabel.delete(0, "end")
#actually makes password
    if password_pool and count > 0:
        thy_password = random.choices(password_pool, k=count)
        the_pass = ''.join(thy_password)
        copy_plabel.insert(0, the_pass)
    elif count == 0:
        copy_plabel.insert(0, "Slider set to 0, no password generated.")
    else:
        copy_plabel.insert(0, "Please select at least one.")

    copy_plabel.configure(state="readonly")

def make_letters():
    print(random.choice(string.ascii_letters))

def make_number():
    print(random.randint(0, 9))

def make_symbol():
    print(random.choice(string.punctuation))


#next the GUI
wlc_label = CTK.CTkLabel(
    app, 
    text="PassCat Generator", 
    font=("Arial", 20, "bold"))
wlc_label.pack(pady=20)

#them cats
the_Scat = CTK.CTkLabel(
    master=app,
    text=ascii_cat_s,
    font=("Consolas", -15),
    justify="left"
)
the_Scat.pack()

the_Ccat = CTK.CTkLabel(
    master=app,
    text=ascii_cat,
    font=("Consolas", -15),
    justify="left"
)
the_Ccat.pack_forget()

the_ocat = CTK.CTkLabel(
    master=app,
    text=ascii_cat_o,
    font=("Consolas", -15),
    justify="left"
)
the_ocat.pack_forget()

#decorating slider
slider_frame = CTK.CTkFrame(
    master=app,
    corner_radius=12
)
slider_frame.pack_forget()

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
    number_of_steps=15, 
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
opt_frame.pack_forget()
opt_frame.grid_columnconfigure(0, weight=1)
opt_label = CTK.CTkLabel(
    master=opt_frame,
    text="OPTIONS:",
    text_color="#A0A5AA",
    font=("Arial", 11, "bold")
)
opt_label.grid(row=0, column=0, sticky="w", padx=(15, 0), pady=(0, 15))

# Letter TXT Label
optL_label = CTK.CTkLabel(
    master=opt_frame,
    text="Add Letters",
    justify="right",
    font=("Arial", 15, "bold")
)
optL_label.grid(row=1, column=0, sticky="w", padx=(30, 0), pady=(0, 10))
# Letter Switch
optL_var = CTK.StringVar(value="off")
optL_switch = CTK.CTkSwitch(
    master=opt_frame,
    text="",
    variable=optL_var,
    onvalue="on",
    offvalue="off"
)
optL_switch.grid(row=1, column=2, sticky="e", padx=(15, 0), pady=(0, 10))

# Number TXT Label
optN_label = CTK.CTkLabel(
    master=opt_frame,
    text="Add Numbers",
    justify="right",
    font=("Arial", 15, "bold")
)
optN_label.grid(row=2, column=0, sticky="w", padx=(30, 0), pady=(0, 10))
# Number Switch
optN_var = CTK.StringVar(value="off")
optN_switch = CTK.CTkSwitch(
    master=opt_frame,
    text="",
    variable=optN_var,
    onvalue="on",
    offvalue="off"
)
optN_switch.grid(row=2, column=2, sticky="e", padx=(15, 0), pady=(0, 10))

# Symbols TXT Label
optS_label = CTK.CTkLabel(
    master=opt_frame,
    text="Add Symbols",
    justify="right",
    font=("Arial", 15, "bold")
)
optS_label.grid(row=3, column=0, sticky="w", padx=(30, 0), pady=(0, 10))
# Symbols Switch
optS_var = CTK.StringVar(value="off")
optS_switch = CTK.CTkSwitch(
    master=opt_frame,
    text="",
    variable=optS_var,
    onvalue="on",
    offvalue="off"
)
optS_switch.grid(row=3, column=2, sticky="e", padx=(15, 0), pady=(0, 10))

#main menu
start_btn = CTK.CTkButton(master=app, text="Start", font=("Arial", 15), width=500, height=45, command=gen_menu)
start_btn.pack(padx=10, pady=5)
stngs_btn = CTK.CTkButton(master=app, text="Settings", font=("Arial", 15), width=500, height=45)
stngs_btn.pack(padx=10, pady=5)
quit_btn = CTK.CTkButton(master=app,
    text="Quit", 
    font=("Arial", 15), 
    fg_color="#A82828",
    hover_color="#6E1D1D",
    width=500, height=45, 
    command=app.quit
)
quit_btn.pack(padx=10, pady=5)

#gen menu
make_btn = CTK.CTkButton(
    master=app, 
    text="Generate", 
    font=("Arial", 15),
    fg_color="#28A83D",
    hover_color="#1D6E20",
    width=500, height=45,
    command=make_password
)
back_btn = CTK.CTkButton(master=app, text="Go Back", font=("Arial", 15), width=500, height=45, command=go_back)
copy_plabel = CTK.CTkEntry(
    master=app,
    font=("Arial", 15),
    placeholder_text="",
    border_width=0,
    width=500, height=45,
    justify="center",
    text_color=("black", "white")
)
copy_plabel.insert(0, "Double Click or Drag me to copy the text!")
copy_plabel.configure(state="readonly")

app.mainloop()
