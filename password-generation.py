import random

#customizing the GUI

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x600")
root.configure(bg="#1f242a")

q = """
1. Generate Password
2. Exit
"""

while True:
    choice = input("Select your option: ")
    if choice == "1":
        print("Which one do you want?") 
