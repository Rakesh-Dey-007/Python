# Import everything from customtkinter module
import customtkinter as ctk
import calendar

# Set appearance mode and theme for the customtkinter application
ctk.set_appearance_mode('System')  # Can be 'Light' or 'Dark'
ctk.set_default_color_theme('green')  # Color themes: 'blue', 'green', 'dark-blue'

# Function to display the calendar for the entered year
def showCal():
    # Create a new window to display the calendar
    new_gui = ctk.CTk()
    
    # Set background color and window properties
    new_gui.configure(fg_color="white")
    new_gui.title("CALENDAR")
    new_gui.geometry("600x600")

    # Fetch the year entered by the user
    fetch_year = int(year_field.get())

    # Get the calendar for the fetched year
    cal_content = calendar.calendar(fetch_year)

    # Create a textbox to display the calendar content
    cal_textbox = ctk.CTkTextbox(new_gui, width=550, height=550, font=("Consolas", 12))
    cal_textbox.insert("0.0", cal_content)  # Insert the calendar text into the textbox
    cal_textbox.configure(state="disabled")  # Make the textbox read-only

    # Place the textbox in the window
    cal_textbox.grid(row=0, column=0, padx=20, pady=20)

    # Start the new window's event loop
    new_gui.mainloop()


# Main application window
if __name__ == "__main__":
    # Create the main window
    gui = ctk.CTk()
    gui.configure(fg_color="#F0F0F0")  # Set a light grey background
    gui.title("CALENDAR")
    gui.geometry("300x300")  # Slightly larger window for better spacing
    gui.resizable(False, False)  # Make the window non-resizable

    # Create a label for "CALENDAR" title with default font
    cal = ctk.CTkLabel(gui, text="CALENDAR", text_color="blue",
                       corner_radius=10, padx=10, font=ctk.CTkFont('Arial', 30))

    # Create a label for entering the year with default font
    year = ctk.CTkLabel(gui, text="Enter Year", text_color="black")

    # Entry box to input the year
    year_field = ctk.CTkEntry(gui, placeholder_text="YYYY", width=150, height=30, corner_radius=8)

    # Create a button to show the calendar
    Show = ctk.CTkButton(gui, text="Show Calendar", fg_color="#FF6347",  # Tomato color
                         text_color="white", command=showCal, hover_color="#FF4500",
                         width=150, height=40, corner_radius=8)

    # Create an exit button to close the application
    Exit = ctk.CTkButton(gui, text="Exit", fg_color="red", text_color="white", command=exit,
                         hover_color="#B22222", width=150, height=40, corner_radius=8)

    # Positioning the widgets on the grid with appropriate padding and alignment
    cal.grid(row=0, column=0, padx=20, pady=20)
    year.grid(row=1, column=0, padx=10, pady=10)
    year_field.grid(row=2, column=0, padx=10, pady=5)
    Show.grid(row=3, column=0, padx=10, pady=20)
    Exit.grid(row=4, column=0, padx=10, pady=5)

    # Start the main loop to display the window
    gui.mainloop()
