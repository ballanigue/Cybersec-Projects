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
