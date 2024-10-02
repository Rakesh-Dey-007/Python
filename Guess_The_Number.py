import customtkinter as ctk
import random
from tkinter import messagebox

# Set appearance mode and theme
ctk.set_appearance_mode("System")

# Initialize the app window
screen = ctk.CTk()
screen.geometry("450x400")
screen.title("Guess The Number")
screen.resizable(False, False)

# Change font family to "Times New Roman"
my_font = ctk.CTkFont(family="Times New Roman", size=30, weight="bold", slant="italic")
my_font2 = ctk.CTkFont(family="Roboto Slab", size=20, weight="bold", slant="italic")

# Global variables
random_number = random.randint(1, 100)  # Generates the random number to guess

# Function to handle the guess
def check_guess(event=None):  # Accept event parameter for "Enter" key binding
    try:
        guess = int(number_entry.get())  # Get the number entered by the user
        if guess < random_number:
            label_2.configure(text="Too Low🤐. Try Again.", text_color="red")
            screen.after(2000, lambda: label_2.configure(text=""))
        elif guess > random_number:
            label_2.configure(text="Too High🤐. Try Again.", text_color="red")
            screen.after(2000, lambda: label_2.configure(text=""))
        else:
            number = f"Correct Number is : {random_number}"
            label_3.configure(text="Congratulations✨. Correct Guess! 🎉", text_color="green")
            label_2.configure(text=number)  # Clear the previous label
            restart_button.pack(pady=(20, 0))  # Show the restart button when the user wins
        number_entry.delete(0, 'end')  # Clear the entry box after checking
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# Function to restart the game
def restart_game():
    global random_number
    random_number = random.randint(1, 100)
    number_entry.delete(0, 'end')  # Clear the entry field
    label_2.configure(text="")
    label_3.configure(text="")
    restart_button.pack_forget()  # Hide the restart button

# Heading
heading = ctk.CTkLabel(screen, text="Number Guessing Game", font=my_font, text_color="#ffdf00")
heading.pack(pady=20)

# Label for number entry
label_1 = ctk.CTkLabel(screen, text="Enter a Number (1-100):", font=ctk.CTkFont(size=20))
label_1.pack(pady=(10, 0))

# Entry field for entering a number
number_entry = ctk.CTkEntry(screen, height=50, width=400, font=ctk.CTkFont(size=20), justify='center')  # Center the text
number_entry.pack(pady=(10, 20))
number_entry.bind("<Return>", check_guess)  # Bind the Enter key to check_guess function

# Button to submit the number
enter_button = ctk.CTkButton(screen, text="Enter", font=my_font2, fg_color="#191919", hover_color="#031273", width=110, height=40, command=check_guess)
enter_button.pack(pady=1)

# Label to display feedback (too high, too low)
label_2 = ctk.CTkLabel(screen, text="", font=my_font2)
label_2.pack(pady=(10, 0))

# Label to display success message
label_3 = ctk.CTkLabel(screen, text="", font=my_font2)
label_3.pack(pady=(10, 0))

# Restart button to reset the game (initially hidden)
restart_button = ctk.CTkButton(screen, text="Restart", command=restart_game, fg_color="transparent", hover_color="#191919", width=120, height=40, font=my_font2, border_color="yellow", border_width=2, text_color="orange")  
restart_button.pack_forget()  # Hide the button initially

screen.mainloop()
