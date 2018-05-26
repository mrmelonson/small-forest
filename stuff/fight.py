#Patrick Fennell z5218631
#base for fighting

from stuff import printing, explore
from stuff import enemy as enemypg
import random

def Fight(name, health, damage, player):
    enemy = enemypg.Enemy(name, health, damage)

    printing.Print("A wild " + enemy.name + " has appeared!")

    while enemy.health > 0:
        choice = ''

        printing.PrintHitByPlayer("Your health is " + str(player.health))
        printing.PrintHitByEnemy(enemy.name + "'s health is " + str(enemy.health))

        printing.PrintOpt("Attack")
        printing.PrintOpt("Counter")
        printing.PrintOpt("Run")

        choice = input().lower()

        if choice == "attack":
            enemy.Take(player, False)
            enemy.Deal(player, False)
        elif choice == "counter":
            enemy.Deal(player, True)
        elif choice == "run":
            printing.Print("You try to make a break for it...")
            if CanRun():
                Run(player)
            else:
                printing.Print("The " + enemy.name + " catches up to you")
                enemy.Deal(player, False)
        else:
            printing.Print("You stumble giving the " + enemy.name + " a chance to attack")
            enemy.Deal(player, False)
    printing.Print("You defeated the " + enemy.name)
    printing.Print("Some coins appear infront of you")
    printing.Print("You pick them up")
    player.AddToInv("gold coin", random.randint(3,6))

def CanRun():
    if random.randint(1,5) == 1:
        return True
    else:
        return False
            
def Run(player):
    printing.Print("You manage to lose them")
    printing.Print("you rest for a little bit after running so far and for so long")
    explore.Idle(player)



