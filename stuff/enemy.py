#Base classes for enemies
from stuff import printing
import random
class Enemy():
    
    enemyCount = 0

    flavour = [" strikes ", " hits ", " violently pushes ", " baps ", " uppercuts ", " bites ", " kicks "]

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.enemyCount += 1 

    def Deal(self, player, counter):
        damage = self.damage
        if counter:
            if random.randint(1,2) == 1:
                self.Take(player, True)
                return
            else:   
                damage = damage * 1.5
                printing.Print("You mess up the counter")

        player.health = player.health - damage
        printing.PrintHitByEnemy(self.name + self.flavour[random.randint(0,len(self.flavour) - 1)] + player.name + " for " + str(damage))
        if player.health <= 0:
            player.HasDied()
    
    def Take(self, player, counter):
        damage = player.attack + player.weapons[player.equipped]
        crit = player.Crit()
        if crit != 1:
            printing.PrintHitByPlayerCrit("Critical! 2x damage!")
            damage = damage * crit
        if counter:
            damage = damage * 2
            printing.PrintHitByPlayer(self.name +  " tries to attack but " + player.name + " counters " + self.name + " for " + str(damage))
        else:
            printing.PrintHitByPlayer(player.name + self.flavour[random.randint(0,len(self.flavour) - 1)] + self.name + " for " + str(damage))
        self.health = self.health - damage





