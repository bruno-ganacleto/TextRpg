import os
from time import sleep

def clear():
    os.system('cls')

def typewrite(text: str, speed: float, pause: float):
    for i in range(len(text)):
        print(text[i], end="", flush=True)
        sleep(speed)
    sleep(pause)