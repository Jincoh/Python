import zombiedice
from zombiedice import ICON, SHOTGUN


def main():
    zombies = (
            #zombiedice.examples.RandomCoinFlipZombie(name = 'Random'),
            #zombiedice.examples.RollsUntilInTheLeadZombie(name = 'Until Leading'),
            #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
            #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
            #MyZombie("My boy"),
            #MyZombie("My boy 1t",  1),
            #MyZombie("My boy 2t", 2),
            #MyZombie2("M2 - 3", 3, 1),
            #MyZombie2("M2 - 2", 2, 1),
            #MyZombie2("M2 - 4", 4, 1),
            #MyZombie2("M2 - 2 - 2", 2, 2),
            MyZombie2("M2 - 3 - 2", 3, 2), #better, better, even
            #MyZombie2("M2 - 4 - 2", 4, 2),
            #MyZombie3("M3 - 3 - 2", 3, 2),
            MyZombie4("M4", 4, 2, 3), #better, better, even
            #MyZombie4("M4 - 5t - 2sg - 4nt", 5, 2, 4), #very even
            #MyZombie4("M4 -5t - 2sg - 5nt", 5, 2, 5), #fairly even
            #MyZombie4("M4 -4t - 2sg - 4nt", 4, 2, 4) #better

 
            )
    zombiedice.runWebGui(zombies = zombies, numGames=1000)




class MyZombie:
    def __init__(self, name, turnlim = 3):
        self.name = name
        self.turnlim = turnlim

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        turns = 0
        while diceRollResults != None:
            if turns < self.turnlim:
                diceRollResults = zombiedice.roll()
                turns += 1
            else:
                break


class MyZombie2:
    def __init__(self, name, turnlim = 3, sglim = 2):
        self.name = name
        self.turnlim = turnlim
        self.sglim = sglim

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        turns = 0
        brains = 0
        shotguns = 0
        while diceRollResults != None:
            shotguns += diceRollResults['shotgun']
            if turns < self.turnlim and shotguns < self.sglim:
                diceRollResults = zombiedice.roll()
                turns += 1

            else:
                break



class MyZombie3:
    def __init__(self, name, turnlim = 3, sglim = 2):
        self.name = name
        self.turnlim = turnlim
        self.sglim = sglim

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        turns = 0
        brains = 0
        shotguns = 0
        while diceRollResults != None:
            shotguns += diceRollResults['shotgun']
            remdice = gameState['CURRENT_CUP']
            red = 0
            green = 0
            yellow = 0

            for x in remdice:
                if x == "red":
                    red += 1
                if x == "green":
                    green += 1
                if x == "yellow":
                    yellow += 1
            
            if turns < self.turnlim and shotguns < self.sglim:
                diceRollResults = zombiedice.roll()
                turns += 1

            elif turns < self.turnlim and (red < (green + yellow) -7):
                diceRollResults = zombiedice.roll()
                turns += 1

            else:
                break

class MyZombie4:
    def __init__(self, name = "M4", turnlim = 3, sglim = 2, amt = 4):
        self.name = "%s - %stl - %ssg - %snt" % (name, turnlim, sglim, amt)
        self.turnlim = turnlim
        self.sglim = sglim
        self.amt = amt

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        turns = 0
        brains = 0
        shotguns = 0
        amtRolledNextTurn = 0
        while diceRollResults != None:
            shotguns += diceRollResults['shotgun']
            amtRolledNextTurn = diceRollResults['brains']
            print("test: " + str(amtRolledNextTurn))
            #remdice = gameState['CURRENT_CUP']
            #red = 0
            #green = 0
            #yellow = 0

            #for x in remdice:
            #    if x == "red":
            #        red += 1
            #    if x == "green":
            #        green += 1
            #    if x == "yellow":
            #        yellow += 1
            
            if turns < self.turnlim and shotguns < self.sglim and amtRolledNextTurn <= self.amt:
                diceRollResults = zombiedice.roll()
                turns += 1

#            elif turns < self.turnlim and (red < (green + yellow) -7):
#                diceRollResults = zombiedice.roll()
#                turns += 1

            else:
                break

if __name__ == "__main__":
    main()


