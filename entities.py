from data import *

class Hero:
    def __init__(self, name):
        self.name = name
        self.moveset = ["Golpear", "Defender", "Esquivar"]
        self.inv = {}
        self.gold = 0

        self.stats = {
             "max_hp": 5,
             "max_posture": 2,
             "speed": 2
        }
        self.stats["current_hp"] = self.stats["max_hp"]
        self.stats["current_posture"] = self.stats["max_posture"]
        
        self.equipment = {
            "weapon": None,
            "armor": None
        }

class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.moveset = ["Golpear", "Defender", "Esquivar"]
        self.level = level
        self.stats = {
            "max_hp": 3,
            "max_posture": 2,
            "speed": 1
        }
        self.stats["current_hp"] = self.stats["max_hp"]
        self.stats["current_posture"] = self.stats["max_posture"]
       
        self.equipment = {
            "weapon": None,
            "armor": None
        }