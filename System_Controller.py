import customtkinter as ctk
import os

# user-defined functions
def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

def close_tabs():
    # This command is for Windows. You can customize it for other operating systems.
    return os.system("taskkill /IM chrome.exe /F")  # This example is for closing Chrome tabs. 


# Create a CustomTkinter window
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

master = ctk.CTk()  # Create a customtkinter window
master.title("System Control")

# Configure window
master.geometry("350x250")
master.resizable(False, False)


# Font settings
heading_font = ctk.CTkFont(family="Times New Roman", size=35, weight="bold", slant="italic")
button_font = ctk.CTkFont(family="Roboto", size=17, weight="normal")
label_font = ctk.CTkFont(family="Roboto", size=15, weight="normal")


# Heading
heading = ctk.CTkLabel(master, text='System Controller', font=heading_font, text_color='cyan')
heading.grid(pady=10, padx=10, row=0, column=0, columnspan=2)

# Labels for the buttons
shutdown_label = ctk.CTkLabel(master, text="Shutdown your PC:", font=label_font)
shutdown_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")  # Label left of shutdown button

restart_label = ctk.CTkLabel(master, text="Restart your PC:", font=label_font)
restart_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")  # Label left of restart button

close_tabs_label = ctk.CTkLabel(master, text="Close All Open Tabs:", font=label_font)
close_tabs_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")  # Label left of close tabs button


# Creating buttons using customtkinter CTkButton
shutdown_btn = ctk.CTkButton(master, text="Shutdown", command=shutdown, font=button_font, fg_color='#00c04b', hover_color='#008631', text_color='black')
shutdown_btn.grid(row=1, column=1, padx=20, pady=10)

restart_btn = ctk.CTkButton(master, text="Restart", command=restart, font=button_font, fg_color='orange', hover_color='#ff7600', text_color='black')
restart_btn.grid(row=2, column=1, padx=20, pady=10)

close_tabs_btn = ctk.CTkButton(master, text="Close Tabs", command=close_tabs, font=button_font, fg_color='#ff5050', hover_color='#d32f2f', text_color='black')
close_tabs_btn.grid(row=3, column=1, padx=20, pady=10)


# Run the application
master.mainloop()
