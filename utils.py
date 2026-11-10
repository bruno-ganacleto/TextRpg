import os
from time import sleep

def clear():
    os.system('cls')

def typewrite(text: str, speed: float, pause: float):
    for i in range(len(text)):
        print(text[i], end="", flush=True)
        sleep(speed)
    sleep(pause)

#def fight(player, enemy):
    #while player.stats["current_hp"] > 0 and enemy.stats["current_hp"] > 0:
        