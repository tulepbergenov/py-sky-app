import os
from threading import Thread
from tkinter import *

from pyowm import OWM
import pyttsx3
from pyowm.utils.config import get_default_config
from PIL import ImageTk, Image

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('ttt', config_dict)


def clean_and_say():
    entry_result.delete(0, END)
    entry_input.delete(0, END)

    def input_say():
        engine_clean_and_say = pyttsx3.init()
        engine_clean_and_say.setProperty('rate', 135)
        engine_clean_and_say.say("Введите город")
        engine_clean_and_say.runAndWait()
    Thread(target=input_say).start()


def click_clean_and_say():
    Thread(target=clean_and_say).start()


def search_and_say():
    entry_result.insert(0, "                                               ")
    inp = str(entry_input.get())
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(inp)
    detailed_status = observation.weather.detailed_status
    entry_result.insert(0, str(detailed_status))

    def city_say():
        engine_say = pyttsx3.init()
        engine_say.setProperty('rate', 135)
        engine_say.say(detailed_status)
        engine_say.runAndWait()
    Thread(target=city_say).start()


def click_search_and_say():
    Thread(target=search_and_say).start()


root = Tk()
root.title("weather_speak")
root.iconbitmap("icon.ico")
root_input = Frame(root)
root_button = Frame(root)
root_button = LabelFrame(text="")
root_result = Frame(root)
root_image = Frame(root)
root_author = Frame(root)

root["bg"] = "#F0F0F0"
root_input["bg"] = "#F0F0F0"
root_button["bg"] = "#F0F0F0"
root_result["bg"] = "#F0F0F0"
root_image["bg"] = "#F0F0F0"
root_author["bg"] = "#F0F0F0"

img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root_image, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

label_input = Label(root_input,
                    text="Город >> ",
                    bg="#F0F0F0",
                    fg="#0182D2",
                    font="Consolas 13")
label_input.pack(side="left")

entry_input = Entry(root_input,
                    width=15,
                    bg="#0182D2",
                    fg="white",
                    font="Consolas 13")
entry_input.pack(side="left")

button_click_search = Button(root_button,
                             text="Узнать погоду",
                             command=click_search_and_say,
                             font="Consolas 13",
                             bg="#0182D2",
                             fg="white",
                             relief="raised",
                             activebackground="white",
                             activeforeground="#0182D2")
button_click_search.pack(side="left")

button_click_clean = Button(root_button,
                            text="Очистить",
                            command=click_clean_and_say,
                            font="Consolas 13",
                            bg="#0182D2",
                            fg="white",
                            relief="raised",
                            activebackground="white",
                            activeforeground="#0182D2")
button_click_clean.pack(side="left")

entry_result = Entry(root_result,
                     width=30,
                     bg="#0182D2",
                     fg="white",
                     font="Consolas 13")
entry_result.pack()

label_author = Label(root_author,
                     text="Студент 1 курса\nСпециальности ИС - 124\nТулепбергенов Даулет",
                     bg="#F0F0F0",
                     fg="#0182D2",
                     font="Consolas 13")
label_author.pack(side="bottom")

root_input.pack()
root_button.pack()
root_result.pack()
root_image.pack()
root_author.pack()
root.mainloop()
