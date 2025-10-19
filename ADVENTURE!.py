#ADVENTURE!

#init modules
from loggy import *

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

#init vars
health = 5.0
inv    = []
time   = "night"

print("A  D  V  E  N  T  U  R  E   W H I T H   A N   E X C L I M A T I O N   P O I N T !")
choice = input('Type "begin" to start the game. Type "help" to view the instructions.\n> ')
if choice.lower() == "help":
    print("The commands are:\n\ttake:\t\tTake the object.\n\tinspect:\tLook at the object.\n\tuse:\t\tuse the object, put an object down down, stick your hand in the object, etc.\n\nHint: the object you need is not always listed.")
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
    global inv
    if c == "inspect sun":
        print("The sun doesn't look normal, you realize upon closer inspection.")
        return True
    if c == "take sun":
        if "ladder" in inv:
            print("You use the ladder to take the sun. It pops right off of the fake ceiling. There is a hole where it was.\n(type \"use hole\" to climb through it.)")
            return True
        else:
            print("It's too far away.")
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

print("You climb through the hole into a dark cave.")
