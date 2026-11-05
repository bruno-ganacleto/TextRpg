from entities import Hero
from utils import *
from time import sleep

player = Hero("???")
name = player.name

def chapter_1(player):
    typewrite(". . .", 0.3, 1)
    sleep(1)
    typewrite(" CAPÍTULO 1", 0.1, 1)
    sleep(1)
    typewrite(" . . .", 0.3, 2)
    
    typewrite("\n*plic*", 0.1, 0.5)
    typewrite(" *plic*", 0.1, 0.5)
    typewrite(" *plic*", 0.1, 1)

    typewrite("   Você acorda com o som das gotas de água atingindo o chão de pedra.", 0.02, 1)
    typewrite(" Sua cabeça lateja,", 0.02, 0.5)
    typewrite(" uma enxurrada de memórias permeia sua mente.", 0.02, 0.5)
    typewrite(" Mas você sente que", 0.02, 0.5)
    typewrite("...", 0.5, 1)
    typewrite(" Há algo faltando.", 0.1, 2)
    
    typewrite("\nVocê se levanta e olha em volta.", 0.02, 1)
    typewrite(" A mesma pedra da qual são feitas as paredes,", 0.02, 0.5)
    typewrite(" faz o chão no qual você dorme.", 0.02, 1)
    typewrite(" Seu único companheiro,", 0.02, 0.5)
    typewrite(" um camundongo,", 0.02, 0.5)
    typewrite(" foge pelas grades da cela,", 0.02, 0.5)
    typewrite(" deixando você com luz fraca da tocha que ilumina o corredor.", 0.02, 1)


chapter_1(player)