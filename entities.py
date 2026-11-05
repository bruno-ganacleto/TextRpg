from time import sleep
class Hero:
    def __init__(self, name):
        self.name = name
        self.moveset = ["Golpear", "Defender", "Esquivar"]
        self.inv = {}
        self.gold = 0
        self.level = 1
        self.exp = 0

        self.stats = {
             "max_hp": 5,
             "current_hp": 5,
             "max_posture": 2,
             "current_posture": 2,
        }
        self.equipment = {
            "weapon": None,
            "armor": None
        }

    def give_exp(self, amount):
        self.exp += amount

    def level_up(self):
        exp_needed = self.level * 10
        level_amount = 0
        while self.exp >= exp_needed:
                self.exp -= exp_needed
                self.level += 1
                level_amount += 1
                exp_needed = self.level * 10