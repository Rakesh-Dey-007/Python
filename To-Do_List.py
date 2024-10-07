import customtkinter as ctk
from tkinter import messagebox

# Global list for storing tasks
tasks_list = []
counter = 1  # Global counter for task numbering

# Function for checking input error
def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty")
        return 0
    return 1

# Function to clear task number field
def clear_taskNumberField():
    taskNumberField.delete(0, 'end')

# Function to clear task entry field
def clear_taskField():
    enterTaskField.delete(0, 'end')

# Function to insert tasks into the text area
def insertTask(event=None):  # Event added for "Enter" key binding
    global counter
    if inputError() == 0:
        return

    content = enterTaskField.get() + "\n"
    tasks_list.append(content)

    # Insert the task in the TextArea
    TextArea.insert('end', f"[ {counter} ] {content}")
    counter += 1

    clear_taskField()

# Function to delete a task based on task number
def deleteTask():
    global counter

    if len(tasks_list) == 0:
        messagebox.showerror("No Task", "There are no tasks to delete")
        return

    number = taskNumberField.get()

    if number == "":
        messagebox.showerror("Input Error", "Please provide a valid task number")
        return

    try:
        task_no = int(number)
        clear_taskNumberField()
        tasks_list.pop(task_no - 1)
        counter -= 1
        TextArea.delete(1.0, 'end')

        # Rewrite the tasks
        for i in range(len(tasks_list)):
            TextArea.insert('end', f"[ {i + 1} ] {tasks_list[i]}")

    except (ValueError, IndexError):
        messagebox.showerror("Input Error", "Invalid task number")

# Driver code
if __name__ == "__main__":
    # Create a customtkinter window
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    gui = ctk.CTk()
    gui.title("ToDo App with CustomTkinter")
    gui.geometry("450x550")  # Increase window size for better layout
    gui.configure(padx=20, pady=20)
    gui.resizable(False, False)

    # Font settings
    heading_font = ctk.CTkFont(family="Times New Roman", size=35, weight="bold", slant="italic")
    button_font = ctk.CTkFont(family="Roboto Slab", size=17, weight="bold")
    subheader_font = ctk.CTkFont(family="Roboto", size=20, weight="normal")
    entry_font = ctk.CTkFont(family="Roboto", size=15, weight="normal")

    # Headline at the top center
    headline = ctk.CTkLabel(gui, text='To-Do List App', font=heading_font, text_color="cyan")
    headline.grid(row=0, column=0, pady=(0,10), columnspan=2, sticky="n")

    # Label and Entry for adding tasks
    enterTask = ctk.CTkLabel(gui, text="Enter Your Task", text_color="grey", font=subheader_font)
    enterTask.grid(row=1, column=0, pady=10, sticky="w")

    enterTaskField = ctk.CTkEntry(gui, width=378, font=entry_font)
    enterTaskField.grid(row=2, column=0, pady=(0,10), columnspan=2, sticky="w")
    
    # Binding the "Enter" key to the task submission
    enterTaskField.bind("<Return>", insertTask)

    # Submit Button
    Submit = ctk.CTkButton(gui, text="Add Task", command=insertTask, width=100, font=button_font, fg_color='#00c04b', hover_color='#008631')
    Submit.grid(row=3, column=1, pady=10)

    # Text area to display tasks
    TextArea = ctk.CTkTextbox(gui, height=200, width=410, font=entry_font)
    TextArea.grid(row=4, column=0, pady=10, columnspan=2)

    # Label and Entry for deleting tasks by number
    taskNumber = ctk.CTkLabel(gui, text="Delete Task Number", text_color="grey", font=subheader_font)
    taskNumber.grid(row=5, column=0, pady=10, sticky="w")

    taskNumberField = ctk.CTkEntry(gui, width=70, font=entry_font)
    taskNumberField.grid(row=6, column=0, pady=10, sticky="w")

    # Delete Button
    deleteButton = ctk.CTkButton(gui, text="Delete Task", command=deleteTask, width=100, font=button_font, fg_color='orange', hover_color='#ff7600')
    deleteButton.grid(row=5, column=1, pady=10)

    # Exit Button
    exitButton = ctk.CTkButton(gui, text="Exit", command=gui.quit, fg_color="red", hover_color='#8b0000', width=100, font=button_font)
    exitButton.grid(row=6, column=1, pady=10)

    gui.mainloop()
