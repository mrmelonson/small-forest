#Patrick Fennell z5218631
#Base for crafting

from stuff import printing, explore

def CanCraft(player):
    if player.inventory['wood'] >= 2:
        return True
    else:
        return False

def Crafting(player):
    choices = []
    choice = ""

    printing.Print("You decide to craft a...")
    if player.inventory['wood'] >= 2:
        printing.PrintOpt("Torch")
        choices.append("torch")

    printing.PrintOpt("Back")
    choices.append("back")
    
    choice = input()
    choice = choice.lower()
    if choice in choices:
        if choice == "torch" and "torch" in choices:
            Craft(player, "torch")
        elif choice == "back":
            explore.Idle(player)
        else:
            Crafting(player)

def Craft(player, item):
    item = item.lower()
    printing.Print("You crafted a " + str(item))
    if item == "torch":
        player.inventory['wood'] = player.inventory['wood'] - 2
        player.AddToInv("Torch", 1)
        if player.inventory['torch'] > 100:
            printing.Print("OMG STOP MAKING TORCHES")
            printing.Print("FINE HERE,")
            printing.Print("You win!! yay now go do something else ffs")
        
    explore.Idle(player)
    

        
    
    
        
        




