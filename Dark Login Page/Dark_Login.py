import customtkinter as ctk
from tkinter import messagebox
import openpyxl
import os
from PIL import Image

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("green")

# Create the main window
root = ctk.CTk()
root.title('Dark Login System')
root.geometry("670x450")  # Adjusted size to resemble the design
root.configure(bg="#f0f0f0")
root.resizable(False, False)

my_font = ctk.CTkFont(family="Times New Roman", size=33, weight="bold", slant="italic")
my_font2 = ctk.CTkFont(family="Roboto Slab", size=17, weight="bold", slant="italic")

# Define custom fonts
header_font = ctk.CTkFont(family="Roboto", size=32, weight="bold")
subheader_font = ctk.CTkFont(family="Roboto", size=20, weight="normal")
label_font = ctk.CTkFont(family="Roboto", size=17)
button_font = ctk.CTkFont(family="Roboto", size=14, weight="bold")

# Define login function
def login(action):
    username = entry1.get()
    password = entry2.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both Username and Password")
    else:
        # Display login success message
        messagebox.showinfo("Success", f"{action} Successful!")
        
        # Print success message to terminal
        print(f"{action} successful with Username: {username}")
        
        # Clear the entry boxes
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')

        # Save data to Excel sheet, along with action type (Login or Sign Up)
        save_to_excel(action, username, password)

def save_to_excel(action, username, password):
    file_path = "login_data.xlsx"

    # Check if the Excel file exists, if not, create it with headers
    if not os.path.exists(file_path):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Login Data"
        sheet.append(["Action", "Username", "Password"])
        workbook.save(file_path)

    # Open the Excel file and append the data
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    sheet.append([action, username, password])
    workbook.save(file_path)

# Create a main frame to hold the image and form side by side
main_frame = ctk.CTkFrame(master=root)
main_frame.pack(pady=0, padx=0, fill="both", expand=True)

# Load and add the image to the left side
image = ctk.CTkImage(Image.open("login.jpg"), size=(330, 450))  # Use your image
image_label = ctk.CTkLabel(master=main_frame, image=image, text="")
image_label.grid(row=0, column=0, rowspan=6, padx=0, pady=0)

# Create the login form frame on the right
form_frame = ctk.CTkFrame(master=main_frame)
form_frame.grid(row=0, column=1, sticky="nsew")

# Add title and subtitle labels
title_label = ctk.CTkLabel(master=form_frame, text="Login to the Darkside", text_color="#ffdf00", font=my_font)
title_label.grid(row=0, column=0, columnspan=2, pady=(20,10), padx=20)

subtitle_label = ctk.CTkLabel(master=form_frame, text="Login to Your Dev Environment.", font=subheader_font)
subtitle_label.grid(row=1, column=0, columnspan=2, pady=(10,20), padx=20)

# Add label and entry for username
username_label = ctk.CTkLabel(master=form_frame, text="Username :", font=label_font)
username_label.grid(row=2, column=0, padx=10, pady=(20,10), sticky='e')

entry1 = ctk.CTkEntry(master=form_frame, placeholder_text="Enter Username", font=label_font)
entry1.grid(row=2, column=1, padx=10, pady=(20,10), sticky='w')

# Add label and entry for password
password_label = ctk.CTkLabel(master=form_frame, text="Password :", font=label_font)
password_label.grid(row=3, column=0, padx=10, pady=(10,20), sticky='e')

entry2 = ctk.CTkEntry(master=form_frame, placeholder_text="Enter Password", font=label_font, show="*")
entry2.grid(row=3, column=1, padx=10, pady=(10,20), sticky='w')

# Add "Remember Me" checkbox and "Forgot password" label
checkbox_frame = ctk.CTkFrame(master=form_frame, fg_color="transparent")
checkbox_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky='nsew')

checkbox = ctk.CTkCheckBox(master=checkbox_frame, text="Remember Me", font=label_font)
checkbox.pack(side="left")

forgot_password = ctk.CTkLabel(master=checkbox_frame, text="Forgot password?", font=label_font)
forgot_password.pack(side="right")

# Add login and sign-up buttons
button_frame = ctk.CTkFrame(master=form_frame, fg_color="transparent")
button_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=(10,20), sticky='nsew')

login_button = ctk.CTkButton(master=button_frame, text="Login", command=lambda: login("Login"), font=my_font2, width=100, height=30)
login_button.pack(side="left", padx=5)

signup_button = ctk.CTkButton(master=button_frame, text="Sign Up", command=lambda: login("Sign Up"), font=my_font2, width=100, height=30)
signup_button.pack(side="right", padx=5)

# Add terms and conditions label
terms_label = ctk.CTkLabel(master=form_frame, text="By signing up, you agree to Dark\nTerms & Conditions & Privacy Policy", font=label_font, justify="center")
terms_label.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

# Start the main event loop
root.mainloop()
