import customtkinter as ctk
from tkinter import PhotoImage
import math


ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("deepblue")


screen = ctk.CTk()
screen.geometry("350x520")
screen.title("Calculator")


icon_image = PhotoImage(file="calculator_img.png")
screen.iconphoto(False, icon_image)


screen.resizable(False, False)

# Configure the grid layout for columns and rows
screen.grid_columnconfigure((0, 1), weight=1)
screen.grid_rowconfigure(0, weight=1)

calculation_area = ctk.CTkEntry(screen, width=310, height=80, font=ctk.CTkFont(size=20))
calculation_area.place(x=20, y=15)


# Function to handle number button clicks
def on_button_click(number):
    current_text = calculation_area.get()  # Get the current text in the entry box
    calculation_area.delete(0, 'end')  # Clear the entry box
    calculation_area.insert('end', current_text + str(number))  # Append the clicked number


# Function to handle operator button clicks
def on_operation_click(operator):
    current_text = calculation_area.get()  # Get the current text in the entry box
    calculation_area.delete(0, 'end')  # Clear the entry box
    calculation_area.insert('end', current_text + operator)  # Append the operator


# Function to handle removing the last character
def on_backspace_click():
    current_text = calculation_area.get()  # Get the current text in the entry box
    if current_text:  # Check if there's anything to delete
        calculation_area.delete(len(current_text)-1, 'end')  # Remove the last character



button_AC = ctk.CTkButton(screen, text="AC", width=50, height=50, font=ctk.CTkFont(size=20),
                          command=lambda: calculation_area.delete(0, 'end'))  # Clear the entry on AC
button_percentage = ctk.CTkButton(screen, text="%", width=50, height=50, font=ctk.CTkFont(size=20),
                                  command=lambda: on_operation_click('%'))
button_x = ctk.CTkButton(screen, text="x", width=50, height=50, font=ctk.CTkFont(size=20),
                         command=lambda: on_backspace_click())
button_devide = ctk.CTkButton(screen, text="/", width=50, height=50, font=ctk.CTkFont(size=20),
                              command=lambda: on_operation_click('/'))



button_7 = ctk.CTkButton(screen, text="7", width=50, height=50, fg_color="#191919",hover_color="#031273",  font=ctk.CTkFont(size=20), command=lambda: on_button_click(7))

button_8 = ctk.CTkButton(screen, text="8", width=50, height=50, fg_color="#191919",hover_color="#031273", font=ctk.CTkFont(size=20), command=lambda: on_button_click(8))

button_9 = ctk.CTkButton(screen, text="9", width=50, height=50, fg_color="#191919",hover_color="#031273",  font=ctk.CTkFont(size=20), command=lambda: on_button_click(9))

button_X = ctk.CTkButton(screen, text="*", width=50, height=50, font=ctk.CTkFont(size=25), command=lambda: on_operation_click('*'))



button_4 = ctk.CTkButton(screen, text="4", width=50, height=50, fg_color="#191919",hover_color="#031273", font=ctk.CTkFont(size=20), command=lambda: on_button_click(4))

button_5 = ctk.CTkButton(screen, text="5", width=50, height=50, fg_color="#191919",hover_color="#031273", font=ctk.CTkFont(size=20), command=lambda: on_button_click(5))

button_6 = ctk.CTkButton(screen, text="6", width=50, height=50, fg_color="#191919",hover_color="#031273", font=ctk.CTkFont(size=20), command=lambda: on_button_click(6))

button_minus = ctk.CTkButton(screen, text="-", width=50, height=50, font=ctk.CTkFont(size=25), command=lambda: on_operation_click('-'))



button_1 = ctk.CTkButton(screen, text="1", width=50, height=50, fg_color="#191919", hover_color="#031273", font=ctk.CTkFont(size=20), command=lambda: on_button_click(1))

button_2 = ctk.CTkButton(screen, text="2", width=50, height=50, fg_color="#191919",hover_color="#031273", font=ctk.CTkFont(size=20), command=lambda: on_button_click(2))

button_3 = ctk.CTkButton(screen, text="3", width=50, height=50, fg_color="#191919", hover_color="#031273", font=ctk.CTkFont(size=20), command=lambda: on_button_click(3))

button_plus = ctk.CTkButton(screen, text="+", width=50, height=50, font=ctk.CTkFont(size=25), command=lambda: on_operation_click('+'))



button_00 = ctk.CTkButton(screen, text="00", width=50, height=50, fg_color="#191919", hover_color="#031273", font=ctk.CTkFont(size=20), command=lambda: on_button_click("00"))

button_0 = ctk.CTkButton(screen, text="0", width=50, height=50, fg_color="#191919",hover_color="#031273", font=ctk.CTkFont(size=20), command=lambda: on_button_click(0))

button_dot = ctk.CTkButton(screen, text=".", width=50, height=50, fg_color="#191919",hover_color="#031273", font=ctk.CTkFont(size=25), command=lambda: on_button_click('.'))

button_equal = ctk.CTkButton(screen, text="=", width=50, height=50, font=ctk.CTkFont(size=25), command=lambda: calculate())



# Function to handle calculation when "=" is clicked
def calculate():
    try:
        result = eval(calculation_area.get())  # Evaluate the expression in the entry box
        calculation_area.delete(0, 'end')  # Clear the entry box
        calculation_area.insert('end', str(result))  # Display the result
    except:
        calculation_area.delete(0, 'end')
        calculation_area.insert('end', 'Error')



# Placing the buttons using grid
button_AC.place(x=25, y=120)
button_AC.configure(fg_color="#000814", hover_color="#031273")

button_percentage.place(x=110, y=120)
button_percentage.configure(fg_color="#000814", hover_color="#031273")

button_x.place(x=195, y=120)
button_x.configure(fg_color="#000814", hover_color="#031273")

button_devide.place(x=280, y=120)
button_devide.configure(fg_color="#000814", hover_color="#031273")


button_7.place(x=25, y=200)
button_8.place(x=110, y=200)
button_9.place(x=195, y=200)
button_X.place(x=280, y=200)
button_X.configure(fg_color="#000814", hover_color="#031273")

button_4.place(x=25, y=280)
button_5.place(x=110, y=280)
button_6.place(x=195, y=280)
button_minus.place(x=280, y=280)
button_minus.configure(fg_color="#000814", hover_color="#031273")

button_1.place(x=25, y=360)
button_2.place(x=110, y=360)
button_3.place(x=195, y=360)
button_plus.place(x=280, y=360)
button_plus.configure(fg_color="#000814", hover_color="#031273")

button_00.place(x=25, y=440)
button_0.place(x=110, y=440)
button_dot.place(x=195, y=440)
button_equal.place(x=280, y=440)
button_equal.configure(fg_color="#ffdc73", text_color="#000814", hover_color="#031273")


screen.mainloop()
