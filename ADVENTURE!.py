#ADVENTURE!

#init modules
from loggy import *
from time import time, sleep
import sys

#init commands
def shortCommands(inp):
    if inp.lower() == "take":
        print("What do you want to take?")
        return True
    if inp.lower() == "inspect":
        print("What do you want to inspect?")
        return True
    if inp.lower() == "use":
        print("What do you want to use?")
        return True
    if inp.lower() == "wander":
        print("You can't do that here.")

def normalFuncs(inp):
    inp = inp.lower()
    shortCommands(inp)
    if health < 0.1:
        sys.exit()

#init vars
health = 5.0
inv    = []
time   = "night"

print("A  D  V  E  N  T  U  R  E   W H I T H   A N   E X C L I M A T I O N   P O I N T !")
choice = input('Type "begin" to start the game. Type "help" to view the instructions.\n> ')
if choice.lower() == "help":
    print("The commands are:\n\ttake:\t\tTake the object.\n\tinspect:\tLook at the object.\n\tuse:\t\tuse the object, put an object down down, stick your hand in the object, etc.\n\twander:\t\twalk around.\nHint: the object you need is not always listed.")
    input("Press enter to begin!")

print("You wake up in a room with a bed and a lamp.")

def room(c):
    doorOpen = False
    lamp     = True
    bedKey   = True
    sawHole  = False
    global time
    global inv
    """if c == "take lamp":
        lamp = False
        print("You now have a lamp!\nThe room is now dark. You can not see.")
        inv += ["lamp"]
        log(inv)
        return True"""
    if c == "use lamp":
        print("You don't see the need to turn off the lamp.")
        return True
    if c == "take bed":
        print("The bed is too heavy to take.")
        return True
    if c == "use bed":
        time = "day"
        print("You sleep in the bed.")
        return True
    if c == "use door":
        print("The door swings open.")
        if time == "day":
            print("You leave the room.")
            return "yay"
        else:
            print("It is night. You decide not to leave yet.")
        return True
    if c == "inspect bed":
        print("It's a bed.")

        return True
    if c == "inspect room":
        print("There is a hole in the wall.")
        return True
    if c == "inspect hole":
        print("You look in the hole. Something looks back at you")
        return True
    if c == "use hole":
        print("Something bit you. You lost half a heart.")
        health -= 0.5
        return True
    if c == "devskip":
        return "yay"
    return False

choice = input("What do you want to do?\n> ")
r = room(choice.lower())
while r != "yay":
    choice = input("What do you want to do?\n> ")
    r = room(choice.lower())
    if r == False:
        print("I don't understand.")

print("You walk outside into a sunny meadow. There is an axe on the ground.")
def meadow(c):
    insp = False
    global inv
    if c == "inspect sun":
        print("The sun doesn't look normal, you realize upon closer inspection.")
        insp = True
        return True
    if c == "take sun":
        if insp == True:
            if "ladder" in inv:
                print("You use the ladder to take the sun. It pops right off of the fake ceiling. There is a hole where it was.\n(type \"use hole\" to climb through it.)")
                return True
            else:
                print("It's too far away.")
        else:
            print("WHAT")
        return True
    if c == "take axe":
        print("You pick up the axe. You now have an axe!")
        inv += ["axe"]
        return True
    if c == "use axe":
        if "axe" in inv:
            print("You cut down the trees. You now have wood!")
            inv += ["wood"]
            return True
        else:
            print("You are not holding the axe.")
            return True
    if c == "use wood":
        if "wood" in inv:
            print("You use the wood to make a ladder!")
            inv += ["ladder"]
            return True
        else:
            print("You don't have wood.")
    if c == "use ladder"):
        print("What for?\nHint: type \"take ###\" to use the ladder")
    if c == "use hole":
        return "yay"
    if c == "devskip":
        return "yay"
              
choice = input("What do you want to do?\n> ")
r = room(choice.lower())
while r != "yay":
    choice = input("What do you want to do?\n> ")
    r = meadow(choice.lower())
    if r == False:
        print("I don't understand.")

print("You climb through the hole into a dark cave. There is a metal on the floor.")

def cave(c):
    global inv
    if c == "inspect metal":
        print("It's flint. Isn't that used for starting fires?")
        return True
    if c == "use flint":
        print("You try to start a fire.")
        for i in range(9):
            print("Tick...")
            log(i+1)
        print("It worked! You now have a torch.")
        inv += ["torch"]
        return True
    if c == "inspect cave":
        if "torch" in inv:
            print("You see a bat. It looks angry. You lost a life.")
            health -= 1
            if health < 0.1:
                print("You died!")
                sys.exit()
        else:
            print("It's too dark.")
        return True
    if c == "wander":
        print("You hear a faint click. use \"inspect click\" to check it out.")
    if c == "inspect click":
        print("You find an even deeper and darker part of the cave.")
    
