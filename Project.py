import tkinter as tk
from tkinter import messagebox
import csv

def get_weather_and_aqi():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    # Read weather data from CSV file
    try:
        with open('weather_data_india.csv', mode='r') as file:  # Added .csv extension
            reader = csv.DictReader(file)
            for row in reader:
                if row['city'].lower() == city.lower():
                    result = (
                        f"Weather in {city}:\n"
                        f"Temperature: {row['temp']}°C\n"
                        f"Humidity: {row['humidity']}%\n"
                        f"Condition: {row['desc']}\n\n"
                        f"Air Quality: {row['aqi']}"
                    )
                    output_label.config(text=result)
                    return
            messagebox.showerror("Error", f"City {city} not found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Weather data file not found.")

# GUI Setup
root = tk.Tk()
root.title("Weather & Air Quality Checker")

tk.Label(root, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Check", command=get_weather_and_aqi).pack(pady=5)

output_label = tk.Label(root, text="", justify="left", font=("Arial", 10), wraplength=300)
output_label.pack(pady=10)

root.mainloop()
