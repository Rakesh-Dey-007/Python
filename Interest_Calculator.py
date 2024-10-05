import customtkinter as ctk
import math
import pyfiglet


text = pyfiglet.figlet_format("Interest Calculator")
print(text)


# Set appearance and color theme
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('green')

# Initialize the window
screen = ctk.CTk()
screen.geometry("380x420")
screen.title('Interest Calculator')
screen.resizable(False, False)

# Fonts
heading_font = ctk.CTkFont(family="Times New Roman", size=35, weight="bold", slant="italic")
button_font = ctk.CTkFont(family="Roboto Slab", size=20, weight="bold", slant="italic")
subheader_font = ctk.CTkFont(family="Roboto", size=18, weight="normal")
entry_font = ctk.CTkFont(family="Roboto", size=15, weight="normal")

# Headline
headline = ctk.CTkLabel(screen, text='Simple Interest\nCalculator', font=heading_font, text_color="#ffdf00")
headline.grid(row=0, column=0, columnspan=4, pady=(10, 0), padx=20)

# Data Entry Section
principle_label = ctk.CTkLabel(screen, text='Principal ($) :', font=subheader_font, text_color='grey')
principle_label.grid(row=1, column=0, pady=(10, 0), padx=20, sticky="w")

principle_entry = ctk.CTkEntry(screen, width=150, font=entry_font)
principle_entry.grid(row=2, column=0, pady=0, padx=20)

rate_label = ctk.CTkLabel(screen, text='Rate (%) :', font=subheader_font, text_color='grey')
rate_label.grid(row=1, column=3, pady=(10, 0), padx=20, sticky="w")

rate_entry = ctk.CTkEntry(screen, width=150, font=entry_font)
rate_entry.grid(row=2, column=3, pady=0, padx=20)

time_label = ctk.CTkLabel(screen, text='Time :', font=subheader_font, text_color='grey')
time_label.grid(row=3, column=0, pady=(10, 0), padx=20, sticky="w")

time_entry = ctk.CTkEntry(screen, width=150, font=entry_font)
time_entry.grid(row=4, column=0, pady=0, padx=20)

year_label = ctk.CTkLabel(screen, text='Year :', font=subheader_font, text_color='grey')
year_label.grid(row=3, column=3, pady=(10, 0), padx=20, sticky="w")

year_values = ["Select", "1", "2", "3", "4", "5"]
year_option = ctk.StringVar()
year_option.set(year_values[0])
year_menu = ctk.CTkOptionMenu(screen, values=year_values, variable=year_option, fg_color="#464646")
year_menu.grid(row=4, column=3, pady=0, padx=20)

# Result labels (initially empty)
principal_result_label = ctk.CTkLabel(screen, text='', font=subheader_font, text_color='grey')
principal_result_label.grid(row=6, column=0, columnspan=4, pady=(10, 0), padx=20)

interest_result_label = ctk.CTkLabel(screen, text='', font=subheader_font, text_color='grey')
interest_result_label.grid(row=7, column=0, columnspan=4, pady=(5, 0), padx=20)

total_result_label = ctk.CTkLabel(screen, text='', font=subheader_font, text_color='grey')
total_result_label.grid(row=8, column=0, columnspan=4, pady=(5, 0), padx=20)

# Function to calculate Simple Interest and show result
def calculate_interest():
    try:
        P = float(principle_entry.get())
        R = float(rate_entry.get())
        T = float(time_entry.get())
        Y = int(year_option.get())
        SI = (P * R * T * Y) / 100
        total_amount = P + SI
        principal_result_label.configure(text=f"Principal Amount: ${P:.2f}")
        interest_result_label.configure(text=f"Total Interest: ${SI:.2f}")
        total_result_label.configure(text=f"Total Amount: ${total_amount:.2f}")
    except ValueError:
        principal_result_label.configure(text="Invalid input, please enter numbers.")
        interest_result_label.configure(text='')
        total_result_label.configure(text='')

# Function to clear the inputs and clear the result labels
def clear_inputs():
    principle_entry.delete(0, ctk.END)
    rate_entry.delete(0, ctk.END)
    time_entry.delete(0, ctk.END)
    principal_result_label.configure(text='')
    interest_result_label.configure(text='')
    total_result_label.configure(text='')

# Buttons for Calculate and Clear
calculate_button = ctk.CTkButton(screen, text="Calculate", font=button_font, command=calculate_interest)
calculate_button.grid(row=5, column=0, pady=20, padx=20, sticky="w")

clear_button = ctk.CTkButton(screen, text="Clear", font=button_font, command=clear_inputs)
clear_button.grid(row=5, column=3, pady=20, padx=(0, 20), sticky="e")

# Run the application
screen.mainloop()
