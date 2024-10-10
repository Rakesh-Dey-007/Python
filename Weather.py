import customtkinter as ctk
import requests
import json
import datetime

# Initialize customtkinter theme
ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# Initialize root window
root = ctk.CTk()
root.title("Weather App")
root.geometry("570x570")

# Display current date and time
dt = datetime.datetime.now()
date_label = ctk.CTkLabel(root, text=dt.strftime('%A, %B %d, %Y'), font=("Helvetica", 18, 'bold'))
date_label.place(x=150, y=20)

time_label = ctk.CTkLabel(root, text=dt.strftime('%I:%M %p'), font=("Helvetica", 30))
time_label.place(x=200, y=60)

# Create a label for the city entry prompt
entry_prompt_label = ctk.CTkLabel(root, text="Enter city name here:", font=("Helvetica", 16))
entry_prompt_label.place(x=200, y=110)  # Place the label above the entry area

# Create the city entry widget and search button
city_name_var = ctk.StringVar()  # Store the city name entered
city_entry = ctk.CTkEntry(root, textvariable=city_name_var, placeholder_text="Enter City Name", width=350, height=40, font=("Helvetica", 15))
city_entry.place(x=100, y=140)

def fetch_weather():
    # Ensure your API key is available
    api_key = "bd5e378503939ddaee76f12ad7a97608"  # Replace with your OpenWeatherMap API key
    city = city_entry.get()
    city_entry.delete(0, 'end')

    # API request to fetch weather details
    try:
        api_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")
        api = json.loads(api_request.content)

        # Extracting weather data
        temp_data = api['main']
        current_temperature = temp_data['temp']
        humidity = temp_data['humidity']
        temp_min = temp_data['temp_min']
        temp_max = temp_data['temp_max']

        coord_data = api['coord']
        longitude = coord_data['lon']
        latitude = coord_data['lat']

        country_data = api['sys']
        country = country_data['country']
        city_name = api['name']

        # Updating the UI with the fetched weather details
        label_temp.configure(text=f"{current_temperature}°C")
        label_lon.configure(text=f"Longitude: {longitude}")
        label_lat.configure(text=f"Latitude: {latitude}")
        label_country.configure(text=country)
        label_city.configure(text=city_name)

        # Change the color of label_temp based on temperature range
        if current_temperature >= 30:
            label_temp.configure(text_color='#ff5050')  # Very hot
        elif 20 <= current_temperature < 30:
            label_temp.configure(text_color='orange')  # Hot
        elif 10 <= current_temperature < 20:
            label_temp.configure(text_color='blue')  # Warm
        else:
            label_temp.configure(text_color='black')  # Cold

    except Exception as e:
        label_city.configure(text="City not found")

# Bind the Enter key to the fetch_weather function
root.bind('<Return>', lambda event: fetch_weather())

# Search Button
city_name_button = ctk.CTkButton(root, text="Search", command=fetch_weather, width=100, height=40, font=("Helvetica", 14), fg_color='#2b35af', hover_color='#000080')
city_name_button.place(x=220, y=200)

# Display labels for weather details
label_city = ctk.CTkLabel(root, text="City", font=("Helvetica", 16, 'bold'))
label_city.place(x=30, y=260)

label_country = ctk.CTkLabel(root, text="Country", font=("Helvetica", 16, 'bold'))
label_country.place(x=150, y=260)

label_lon = ctk.CTkLabel(root, text="Longitude", font=("Helvetica", 14))
label_lon.place(x=30, y=300)

label_lat = ctk.CTkLabel(root, text="Latitude", font=("Helvetica", 14))
label_lat.place(x=150, y=300)

# Temperature Display
label_temp = ctk.CTkLabel(root, text="--", font=("Helvetica", 100, 'bold'), text_color='#00c04b')
label_temp.place(x=90, y=350)

# Note about temperature unit
note = ctk.CTkLabel(root, text="All temperatures in degree Celsius", font=("Helvetica", 10, 'italic'))
note.place(x=200, y=520)

# Run the application
root.mainloop()
