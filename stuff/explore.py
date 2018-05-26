#Patrick Fennell z5218631
#base for locations in the game

import random
from stuff import printing, craft, fight

def Explore(player):
    num = random.randint(0,6)
    printing.Print("You walk around for a bit")
    if num == 1:
        printing.Print("You come across a small river")
        printing.Print("You cant see a way across and it's too cold to swim")
        River(player)
    elif num == 2:
        printing.Print("you come across a strange rock...")
        printing.Print("On closer inspection it is just a normal rock")
        if ("dagger" in player.inventory) == False:
            printing.Print("Oh there is a dagger lying on the ground near the rock!")
            player.AddToInv("dagger", 1)
            printing.PrintHitByPlayerCrit("HINT: you can equip this! (check inv)")
        Idle(player)
    elif num == 3:
        printing.Print("You stumble across a small cave")
        printing.Print("It looks dark inside")
        if player.inventory['torch'] > 0:
            Cave(player)
        else:
            printing.Print("Hmm, it looks too dark to explore")
            printing.Print("Maybe if you had a torch...")
            Idle(player)
    elif num == 5:
        fight.Fight("Wolf", random.randint(20,25), random.randint(2,5), player)
        Idle(player)
    elif num == 6:
        fight.Fight("Bear", random.randint(45,55), random.randint(5,6), player)
        Idle(player)
    else:
        printing.Print("You find nothing of interest")
        printing.Print("You seem more lost now...")
        Idle(player)

def CollectWood(player):
    printing.Print("You go to collect wood")
    printing.Print("Amazingly in a forrest of trees you find some!")
    player.AddToInv("wood", random.randint(1,3))
    Idle(player)

def Idle(player):
    choice = ""
    choices = []
    printing.Print("You are idle")
    printing.Print("What would you like to do?")

    if (player.inventory['wood'] > 2) == False:
        printing.PrintOpt("Collect wood")
        choices.append("collect wood")

    if craft.CanCraft(player):
        printing.PrintOpt("Craft")
        choices.append("craft")

    printing.PrintOpt("Explore")
    choices.append("explore")

    printing.PrintOpt("Check inventory (inv)")
    choices.append("inv")

    printing.PrintOpt("Check status (stats)")
    choices.append("stats")

    if player.health < player.maxhealth:
        printing.PrintOpt("Rest")
        choices.append("rest")
    
    choice = input()
    choice = choice.lower()
    if choice in choices:
        if choice == "collect wood" and "collect wood" in choices:
            CollectWood(player)
        elif choice == "explore" and "explore" in choices:
            Explore(player)
        elif choice == "inv":
            player.CheckInv()
            Idle(player)
        elif choice == "rest" and "rest" in choices:
            printing.Print("You rest for a bit")
            player.Heal(10)
            Idle(player)
        elif choice == "craft" and "craft" in choices:
            craft.Crafting(player)
        elif choice == "stats":
            player.PrintStatus()
            Idle(player)
        else:
            Idle(player)
    else:
        Idle(player)

def River(player):
    choice = ''

    while choice != 'y' and choice != 'n':
        printing.PrintOpt("Investigate river? (y/n?)")
        choice = input() 

    if choice == 'y':
        printing.Print("You walk down closer to the river")
        printing.Print("You see a pebble")

        choice = ''

        while choice != 'y' and choice != 'n':
            printing.PrintOpt("Pick up pebble? (y/n?)")
            choice = input() 

        if choice == 'y':
            printing.Print("You decide to pick up the pebble")
            player.AddToInv("pebble", 1)
        else:
            printing.Print("You do not need a pebble at this time")

        printing.Print("you investigate a bit further...")
        if random.randint(1,3) == 3:
            printing.Print("You see somthing shiny in the water...")
            printing.Print("Wow you found some gold coins!")
            player.AddToInv("gold coin", random.randint(1,5))
        else:
            printing.Print("you don't find anything of interest")
        Idle(player)        
    else:   
        printing.Print("You decide to turn back")
        Idle(player)

def Cave(player):
    choice = ''

    while choice != 'y' and choice != 'n':
        printing.PrintOpt("Investigate Cave? (y/n?) (will use 1 torch)")
        choice = input() 

    if choice == 'y':
        printing.Print("You light a torch and head inside")
        if player.hasEnteredCave == False:
            player.hasEnteredCave = True
            player.RemoveFromInv("torch", 1)
            smallCave(player)
        else:
            pass
    else:
        printing.Print("You decide not to enter...")
        Idle(player)

def smallCave(player):
    printing.Print("The cave is slightly wet and has moss on the walls")
    printing.Print("You keep walking deeper into the cave")
    printing.Print("You come across a steel sword laying at the end of the cave!")
    player.AddToInv("steel sword", 1)
    printing.Print("You equip the steel sword")
    printing.PrintItem("steel sword equipped!")
    player.equipped = "steel sword"
    printing.Print("As tou turn around a small glowing object catches your eye")
    printing.Print("You investigate the small object...")
    printing.Print("It seems to be some sort of glowing green rock")
    printing.Print("Suddenly your body fills with massive amounts of energy and the glow disapears")
    printing.Print("You feel more powerful!")
    printing.PrintItem("You health has increased to 150!")
    player.maxhealth = 150
    player.health = 150
    printing.Print("You exit the cave")
    printing.Print("As you exit the cave something lands infront of you and looks quite angry")
    fight.Fight("Large Angry Dragon", 200, 10, player)
    printing.Print("After the battle you rest")
    Idle(player)