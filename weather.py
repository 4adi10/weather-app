import tkinter as tk
import requests
from PIL import Image, ImageTk

# Your API key from Weatherbit
API_KEY = '8d315bca16984ed0a87ee0e5104f5fd9'
API_URL = 'http://api.weatherbit.io/v2.0/current'

def get_weather(city):
    params = {'city': city, 'key': API_KEY}
    response = requests.get(API_URL, params=params)
    data = response.json()
    return data

def display_weather():
    city = entry.get()
    data = get_weather(city)
    
    if 'data' not in data:
        label_error.config(text="City not found!")
        return

    # Extract weather info
    temperature = data['data'][0]['temp']
    weather = data['data'][0]['weather']['description']

    # Display temperature and condition
    label_temp.config(text=f"Temperature: {temperature}°C")
    label_weather.config(text=f"Weather: {weather.capitalize()}")

    # Show different images based on weather condition
    if 'clear' in weather.lower():
        weather_img = Image.open("sunny.gif")
    elif 'rain' in weather.lower():
        weather_img = Image.open("rainy.gif")
    elif 'snow' in weather.lower():
        weather_img = Image.open("snowy.gif")
    elif 'cloud' in weather.lower():
        weather_img = Image.open("cloudy.gif")
    else:
        weather_img = Image.open("default.gif")  # Default image if no match is found

    # Ensure the image is animated
    weather_img = ImageTk.PhotoImage(weather_img)
    label_image.config(image=weather_img)
    label_image.image = weather_img
    label_error.config(text="")  # Clear any error message

# GUI Setup
root = tk.Tk()
root.title("Weather App with Animations")

# Welcome Label
label_welcome = tk.Label(root, text="Weatherio", font=('Helvetica', 14, 'bold'))
label_welcome.pack(pady=10)

# City Input
label_city = tk.Label(root, text="Enter City:", font=('Helvetica', 12))
label_city.pack()

entry = tk.Entry(root, font=('Helvetica', 12))
entry.pack(pady=5)

# Get Weather Button
button = tk.Button(root, text="Get Weather", command=display_weather, font=('Helvetica', 12))
button.pack(pady=10)

# Temperature and Weather Labels
label_temp = tk.Label(root, text="", font=('Helvetica', 12))
label_temp.pack()

label_weather = tk.Label(root, text="", font=('Helvetica', 12))
label_weather.pack()

# Error Message (If city is not found)
label_error = tk.Label(root, text="", font=('Helvetica', 12), fg='red')
label_error.pack()

# Weather Image (GIF)
label_image = tk.Label(root)
label_image.pack(pady=10)

# Run the app
root.mainloop()
