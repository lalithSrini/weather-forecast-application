from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather Forecast")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getweather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        timezone.config(text=result)
        long_1at.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude),4}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I : %M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

    # Weather

        data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=6219ccbc4de0d4bd7bcc19f189658b2a").json()

        condition = data['weather'][0]['main']

        description = data['weather'][0]['description']
        temp = int(data['main']['temp'] - 273.15)
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        t.config(text=(temp, "°"), font=("Algerian", 55))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather Forecast ","Invalid Entry!!")



# Search Box
search_image = PhotoImage(file="Images/search.png")
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="Images/search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getweather)
myimage_icon.place(x=390, y=34)

# Logo

logo_image = PhotoImage(file="Images/logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# Bottom box

Frame_image = PhotoImage(file="Images/box.png")
Frame_myimage = Label(image=Frame_image)
Frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time

name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Label

label1 = Label(root, text="WIND", font=("Helvatica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvatica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=225, y=400)

label3 = Label(root, text="DISCRIPTION", font=("Helvatica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvatica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 7, "bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

timezone = Label(root,font=("Helvetica",20),fg="black")
timezone.place(x=650,y=20)


long_1at = Label(root,font=("Helvetica",10),fg="black")
long_1at.place(x=650,y=50)

root.mainloop()
