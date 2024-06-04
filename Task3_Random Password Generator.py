import random
import string
import tkinter as tk
from tkinter import messagebox

def password_generator():
    global uname_enter
    global pass_enter
    
    username = uname_enter.get()
    password_length = int(entry.get())
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    messagebox.showinfo("Generated Password",
                        f"Username: {username}\nPassword Length: {password_length}\nGenerated Password: {password}")

def save_password():
    messagebox.showinfo("Save", "Password saved successfully!")

def reset_fields():
    entry.delete(0, 'end')

# Create the main window
root = tk.Tk()
root.title("Secure Password Generator")

# Username input
username_label = tk.Label(root, text="Enter Username:")
username_label.pack()
uname_enter = tk.Entry(root)
uname_enter.pack()

# Password length input
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()
entry = tk.Entry(root)
entry.pack()

# Generate Password button
generate_button = tk.Button(root, text="Generate Password", command=password_generator)
generate_button.pack()

# Save button
save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.pack()

# Reset button
reset_button = tk.Button(root, text="Clear Fields", command=reset_fields)
reset_button.pack()

root.mainloop()
