import customtkinter as ctk
import string

# Setting up the appearance and color theme
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')


# Initialize screen
screen = ctk.CTk()
screen.geometry('400x500')
screen.title("Password Strength Checker")
screen.configure(bg="#f0f0f0")
screen.resizable(False, False)

my_font = ctk.CTkFont(family="Times New Roman", size=30, weight="bold", slant="italic")
my_font2 = ctk.CTkFont(family="Roboto Slab", size=17, weight="bold", slant="italic")


# Variable to track password visibility state
password_visible = False


# Function to check password strength
def check_password_strength():
    password = password_entry.get()
    strength = 0
    remarks = ""
    lower_case = upper_case = num_count = space_count = special_count = 0

    # Counting character types
    for char in password:
        if char in string.ascii_lowercase:
            lower_case += 1
        elif char in string.ascii_uppercase:
            upper_case += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            space_count += 1
        else:
            special_count += 1

    # Strength evaluation
    if lower_case > 0:
        strength += 1
    if upper_case > 0:
        strength += 1
    if num_count > 0:
        strength += 1
    if space_count > 0:
        strength += 1
    if special_count > 0:
        strength += 1

    # Remarks based on the strength score
    if strength == 1:
        remarks = "Very weak password.\n Please change it."
    elif strength == 2:
        remarks = "Weak password.\n Consider a stronger one."
    elif strength == 3:
        remarks = "Okay password,\n but could be improved."
    elif strength == 4:
        remarks = "Strong password!"
    elif strength == 5:
        remarks = "Very strong password!"

    # Display the result in the GUI
    result_label.configure(text=f"Strength: {strength}/5\nRemarks: {remarks}")
    details_label.configure(text=f"Lowercase: {lower_case}, Uppercase: {upper_case},\nDigits: {num_count}, "
                                 f"Spaces: {space_count}, Special: {special_count}")



# Function to toggle password visibility
def toggle_password_visibility():
    global password_visible
    if password_visible:
        password_entry.configure(show="*")
        see_button.configure(text="Decrypt")
        password_visible = False
    else:
        password_entry.configure(show="")
        see_button.configure(text="Encrypt")
        password_visible = True


# Function to clear the password entry field
def clear_password_entry():
    password_entry.delete(0, 'end')
    result_label.configure(text="")
    details_label.configure(text="")


# Screen components
heading = ctk.CTkLabel(screen, text='Password Strength Checker', font=my_font, text_color="#ffdf00")
heading.pack(pady=20)

label_1 = ctk.CTkLabel(screen, text="Enter Password :", font=ctk.CTkFont(size=20))
label_1.pack(pady=(10, 0))

# Password entry field
password_entry = ctk.CTkEntry(screen, height=50, width=300, font=ctk.CTkFont(size=20), justify='center', show='*')  # Center the text, hide characters
password_entry.pack(pady=(10, 20))

# Frame to hold the See and Clear buttons side by side
button_frame = ctk.CTkFrame(screen, fg_color="#222224")
button_frame.pack(pady=(20, 20))

# Clear button (left of See button)
clear_button = ctk.CTkButton(button_frame, text="Clear", fg_color="#191919", hover_color="#031273", font=my_font2, width=100, height=40, command=clear_password_entry)
clear_button.grid(row=0, column=0, padx=00)

# See button (right of Clear button)
see_button = ctk.CTkButton(button_frame, text="Decrypt Password", fg_color="#191919", hover_color="#031273", font=my_font2, width=180, height=40, command=toggle_password_visibility)
see_button.grid(row=0, column=1, padx=(20,0))


# Button to check password strength
check_strength = ctk.CTkButton(screen, text="Check Strength", fg_color="#191919", hover_color="#031273", font=my_font2,width=180, height=40, command=check_password_strength)
check_strength.pack(pady=(10, 20))

# Label to show results
result_label = ctk.CTkLabel(screen, text="", font=ctk.CTkFont(size=20), text_color="#00ff00")
result_label.pack(pady=(10, 10))

# Label to show details of the password composition
details_label = ctk.CTkLabel(screen, text="", font=ctk.CTkFont(size=18), text_color="#000000")
details_label.pack(pady=(10, 10))

# Start the GUI loop
screen.mainloop()
