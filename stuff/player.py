#functions and storage vars for player
import random
from stuff import printing, explore

class Players():

    health = 100
    maxhealth = 100
    attack = 5
    location = ""
    weapons = {'dagger' : 5, 
            'fists' : 1, 
            'steel sword' : 10}

    hasEnteredCave = False

    equipped = "fists"

    inventory = {'wood': 0,
            'pebble' : 0,
            'gold coin' : 0,
            'torch' : 0}
    
    def __init__(self, name):
        self.name = name

    def Heal(self, amount):
        oldhealth = self.health
        self.health += amount
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        printing.PrintHitByPlayer("You healed " + str(self.health - oldhealth) + " health")

    def Equip(self):
        printing.Print("Which item would you like to equip?")
        choice = ""
        choices = []
        for item in self.weapons:
            if item in self.inventory and self.inventory[item] > 0:
                printing.PrintOpt(item.lower())
                choices.append(item.lower())
        choice = input().lower()
        if choice in choices:
            self.equipped = choice
            printing.PrintItem(choice + " equipped!")
            return
        elif choice == "back":
            explore.Idle(self)
        else:
            self.Equip()
        

    def CanEquip(self):
        for item in self.weapons:
            if item in self.inventory and self.inventory[item] > 0:
                return True
            else:
                pass
        return False

    def AddToInv(self, item, amount):
        item = item.lower()
        if (item in self.inventory) == False:
            self.inventory[item] = 0
        self.inventory[item] = self.inventory[item] + amount
        printing.PrintGain("You gained " + str(amount) + " " + str(item) + "!")

    def RemoveFromInv(self, item, amount):
        s = ""
        item = item.lower()
        if (item in self.inventory) == False:
            return
        self.inventory[item] = self.inventory[item] - amount
        if self.inventory[item] < 1:
            self.inventory[item] = 0
        if (amount == 1) == False:
            s = "s"
        printing.PrintGain(str(amount) + " " + str(item) + s + " removed")

    def IsWeapon(self, item):
        if item in self.weapons:
            return "(Equippable)"
        else:
            return ""

    def CheckInv(self):
        i = 0
        for key, value in self.inventory.items():
            if value < 1:
                pass
            else:
                printing.PrintItem(key + " x " + str(value) + "     " + self.IsWeapon(key))
                i+=1
        if i < 1:
            printing.Print("You are not carrying anything")
        if self.CanEquip():
            while True:
                choice = ""
                printing.PrintOpt("Equip a weapon? (y/n)")
                choice = input().lower()
                if choice == "y":
                    self.Equip()
                    explore.Idle(self)
                elif choice == "n":
                    explore.Idle(self)
                else:
                    pass

    def HasDied(self):
        printing.Print("Well...")
        printing.Print("Looks like you have died")
        printing.Print("That sucks huh :/")
        exit()

    def Crit(self):
        if random.randint(1,4) == 4:
            return 2
        else:
            return 1

    def PrintStatus(self):
        printing.PrintHitByPlayer("Your health is " + str(self.health)) 
        printing.PrintHitByPlayer("Your attack is " + str(self.attack + self.weapons[self.equipped]))
        printing.PrintHitByPlayer("Your equiped weapon is " + str(self.equipped))

    