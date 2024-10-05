# import modules
import customtkinter as ctk
import winapps

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('green')

# function to attach output
def app():
    for item in winapps.search_installed(name_entry.get()):
        name.set(item.name)
        version.set(item.version)
        Install_date.set(item.install_date)
        publisher.set(item.publisher)
        uninstall_string.set(item.uninstall_string)
    name_entry.delete(0, 'end')

# Create main window
master = ctk.CTk()
master.title("Search Install Application")
master.geometry("500x450")
master.resizable(False, False)

# Fonts
heading_font = ctk.CTkFont(family="Times New Roman", size=35, weight="bold", slant="italic")
button_font = ctk.CTkFont(family="Roboto Slab", size=20, weight="bold", slant="italic")
subheader_font = ctk.CTkFont(family="Roboto", size=18, weight="normal")
entry_font = ctk.CTkFont(family="Roboto", size=15, weight="normal")

# Variable Classes in tkinter
name = ctk.StringVar()
version = ctk.StringVar()
Install_date = ctk.StringVar()
publisher = ctk.StringVar()
uninstall_string = ctk.StringVar()

# Headline positioned using grid
headline = ctk.CTkLabel(master, text='Search Installed\nApplication Details', font=heading_font, text_color="#ffdf00")
headline.grid(row=0, column=0, columnspan=3, pady=20)

# Labels and Entry Widgets
ctk.CTkLabel(master, text="Enter App name:", font=subheader_font).grid(row=1, column=0, padx=10, pady=10, sticky="w")
ctk.CTkLabel(master, text="Name:", font=subheader_font).grid(row=3, column=0, padx=10, pady=10, sticky="w")
ctk.CTkLabel(master, text="Version:", font=subheader_font).grid(row=4, column=0, padx=10, pady=10, sticky="w")
ctk.CTkLabel(master, text="Install Date:", font=subheader_font).grid(row=5, column=0, padx=10, pady=10, sticky="w")
ctk.CTkLabel(master, text="Publisher:", font=subheader_font).grid(row=6, column=0, padx=10, pady=10, sticky="w")
ctk.CTkLabel(master, text="Uninstall String:", font=subheader_font).grid(row=7, column=0, padx=10, pady=10, sticky="w")

# Displaying values
ctk.CTkLabel(master, textvariable=name).grid(row=3, column=1, sticky="w")
ctk.CTkLabel(master, textvariable=version).grid(row=4, column=1, sticky="w")
ctk.CTkLabel(master, textvariable=Install_date).grid(row=5, column=1, sticky="w")
ctk.CTkLabel(master, textvariable=publisher).grid(row=6, column=1, sticky="w")

# Uninstall String label with text wrapping (wraplength set to 400 pixels)
ctk.CTkLabel(master, textvariable=uninstall_string, wraplength=200).grid(row=7, column=1, sticky="w")

# Input and Button
name_entry = ctk.CTkEntry(master, width=200, font=entry_font)
name_entry.grid(row=1, column=1, padx=10, pady=10)

button = ctk.CTkButton(master, text="Show", command=app, font=button_font, width=50)
button.grid(row=1, column=2, padx=10, pady=10)

# Bind Enter key to start search
def on_enter_key(event):
    app()

master.bind('<Return>', on_enter_key)

# Main loop
master.mainloop()
