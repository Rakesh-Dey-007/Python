import sounddevice as sd
import soundfile as sf
import customtkinter as ctk
import os

# Global variable for recording
is_recording = False
fs = 44100  # Lowered sample rate for compatibility
duration = 5
myrecording = None

# Check available devices
devices = sd.query_devices()
print(devices)

# Set your input device ID here after checking available devices
input_device_id = 1  # Replace with the actual device ID from your query_devices() output

# Function to start recording
def Voice_rec():
    global is_recording, myrecording
    if not is_recording:
        is_recording = True
        try:
            myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, device=input_device_id)
            sd.wait()
            status_label.configure(text="Recording...")
        except Exception as e:
            status_label.configure(text=f"Error: {e}")

# Function to stop recording
def stop_recording():
    global is_recording
    if is_recording:
        is_recording = False
        status_label.configure(text="Recording stopped.")

# Function to save the recording
def save_audio():
    global myrecording
    if myrecording is not None:
        sf.write('my_Audio_file.flac', myrecording, fs)
        status_label.configure(text="Recording saved as 'my_Audio_file.flac'.")
    else:
        status_label.configure(text="No recording available to save.")

# Function to play the saved recording
def play_audio():
    if os.path.exists('my_Audio_file.flac'):
        data, fs = sf.read('my_Audio_file.flac', dtype='float32')
        sd.play(data, fs)
        sd.wait()
        status_label.configure(text="Playing the audio file.")
    else:
        status_label.configure(text="No audio file found to play.")

# Set up customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create the main window
master = ctk.CTk()
master.geometry("360x270")
# master.resizable(False, False)
master.title("Voice Recorder")

# font
heading_font = ctk.CTkFont(family="Times New Roman", size=35, weight="bold")

# Create and place label
label = ctk.CTkLabel(master, text="Voice Recorder", font=heading_font, text_color='cyan')
label.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

# Status label to show current status
status_label = ctk.CTkLabel(master, text="Status: Ready", font=("Arial", 14))
status_label.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

# Create and place Start Recording button
start_button = ctk.CTkButton(master, text="Start Recording", command=Voice_rec, fg_color='#00c04b', hover_color='#008631', text_color='black')
start_button.grid(row=2, column=0, padx=20, pady=10)

# Create and place Stop Recording button
stop_button = ctk.CTkButton(master, text="Stop Recording", command=stop_recording, fg_color='#ff5050', hover_color='#d32f2f', text_color='black')
stop_button.grid(row=2, column=1, padx=20, pady=10)

# Create and place Save button
save_button = ctk.CTkButton(master, text="Save Recording", command=save_audio, fg_color='orange', hover_color='#ff7600', text_color='black')
save_button.grid(row=3, column=0, padx=20, pady=10)

# Create and place Play button
play_button = ctk.CTkButton(master, text="Play Recording", command=play_audio, fg_color='#2b35af', hover_color='#000080')
play_button.grid(row=3, column=1, padx=20, pady=10)

# Start the main loop
master.mainloop()
