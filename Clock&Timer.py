import time
import customtkinter as ctk
import pyfiglet
from colorama import Fore


highlight = pyfiglet.figlet_format('Digital Timer !')
print(highlight)


# Using colorama to change the color of output to blue

# styled_text=pyfiglet.figlet_format('Digital Timer !',font= 'doom')
# print(Fore.BLUE + styled_text)


# Initialize the screen
screen = ctk.CTk()
screen.geometry('400x350')
screen.title('Digital Timer Clock')
screen.resizable(False, False)

# Fonts
my_font = ctk.CTkFont(family="Times New Roman", size=35, weight="bold", slant="italic")
button_font = ctk.CTkFont(family="Roboto Slab", size=20, weight="bold", slant="italic")
subheader_font = ctk.CTkFont(family="Roboto", size=20, weight="normal")

# Heading label
heading = ctk.CTkLabel(screen, text='Digital Timer Clock', font=my_font, text_color="#ffdf00")
heading.pack(pady=20)

# Instruction label
text = ctk.CTkLabel(screen, text='Set Timer in Seconds', font=subheader_font, text_color='grey')
text.pack(pady=(0, 20))

# Timer entry field
timer_entry = ctk.CTkEntry(screen, height=50, width=300, font=ctk.CTkFont(size=20), justify='center')
timer_entry.pack(pady=10)

# Countdown label (to display the countdown)
countdown_label = ctk.CTkLabel(screen, text='', font=ctk.CTkFont(size=25), text_color="red")
countdown_label.pack(pady=10)

# Countdown function
def start_countdown():
    try:
        total_time = int(timer_entry.get())  # Get the input time in seconds
        while total_time >= 0:
            minutes, seconds = divmod(total_time, 60)
            time_display = f'{minutes:02}:{seconds:02}'
            countdown_label.configure(text=time_display)
            screen.update()
            time.sleep(1)
            total_time -= 1
        timer_entry.delete(0, 'end')
        countdown_label.configure(text="Time's Up!")
    except ValueError:
        countdown_label.configure(text="Invalid Input!")

# Start button functionality
enter_button = ctk.CTkButton(screen, text='Start', font=button_font, fg_color="#191919", hover_color="#031273", 
                             height=40, width=110, command=start_countdown)
enter_button.pack(pady=20)


# Bind Enter key to start countdown
def on_enter_key(event):
    start_countdown()
    # timer_entry.delete(0, 'end')

screen.bind('<Return>', on_enter_key) 

# Run the main screen loop
screen.mainloop()
