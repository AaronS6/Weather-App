import tkinter
import weather
from PIL import Image, ImageTk

mainWindow = tkinter.Tk()

mainWindow.geometry("300x500")

mainWindow.title("Weather app by Aaron")

mainWindow.config(bg="#4BBFCA")


cloud_img = Image.open("cloud.png")
snow_img = Image.open("snow.png")
sun_img = Image.open("sun.png")



cloud_img = cloud_img.resize((150, 150))
snow_img = snow_img.resize((150, 150))
sun_img = sun_img.resize((150, 150))


cloud_img_tk = ImageTk.PhotoImage(cloud_img)
snow_img_tk = ImageTk.PhotoImage(snow_img)
sun_img_tk = ImageTk.PhotoImage(sun_img)


title = tkinter.Label(text="Weather app", bg=mainWindow['bg'],font=('Arial',20,"bold"))
title.pack(pady=20)

countryPrompt = tkinter.Label(text="Country", bg=mainWindow['bg'])
countryPrompt.pack()

countryBox = tkinter.Entry()
countryBox.pack(pady=5)

cityPrompt = tkinter.Label(text="City", bg=mainWindow['bg'])
cityPrompt.pack()

cityBox = tkinter.Entry()
cityBox.pack(pady=5)

def getWeather():
    temperature = weather.get_weather(cityBox.get(),countryBox.get())
    if temperature:
        result.config(text=f"The temperature in {cityBox.get()},{countryBox.get()} is {temperature}C")
        if temperature < 0:
            image_result.config(image=snow_img_tk)
        elif temperature > 25:
            image_result.config(image=sun_img_tk)
        else:
            image_result.config(image=cloud_img_tk)
    else:
        result.config(text=f"Temperature unavailable")

button = tkinter.Button(text="Get Weather",command=getWeather)
button.pack(pady=5)

image_result = tkinter.Label(bg=mainWindow['bg'])
image_result.pack(pady=5)


result = tkinter.Label(text="", bg=mainWindow['bg'],font=("Arial",10,"italic"))
result.pack(pady=10)





#run our application
mainWindow.mainloop()