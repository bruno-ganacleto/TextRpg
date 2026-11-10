from entities import *
from utils import *
from time import sleep
from data import *

player = Hero("Carlos")
enemy = Inimigo("Goblin", 0)

print(enemy.stats["current_hp"])

moves["Golpear"](player, enemy)

print(enemy.stats["current_hp"])