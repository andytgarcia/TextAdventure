import os
import time
from colorama import Fore
from colorama import Style
from colorama import Back
import random

# story: awake in hospital
level = 1
health = 100
choice = ""
attack = ""
playerState = {"start": True,
               "end": False,
               "door": False}

inventory = []
location = "hospitalBunker"



def combat(enemy, Ehealth, Eattack, lvl) :
    global health
    global attack
    global level
    while Ehealth > 0 and health > 0:
        print("Inventory: " + str(inventory))
        attack = input("What attack will you use? ")
        attack.lower()
        print()
        if attack.find("sword") >= 0:
            damage = random.choice([1,2,3,4,5,6,7,8,9,10] * level)
            print("You swung your sword and do " + str(damage) + " damage!")
        elif attack.find("fist") >= 0:
            damage = random.choice([1,2,3,4,5] * level)
            print("You go for a punch and do " + str(damage) + " damage")
        Ehealth = Ehealth - damage
        if Ehealth > 0:
            Edamage = random.choice([1, 2, 3, 4, 5]) * lvl
            print(str(enemy) + " strikes and uses " + str(Eattack) + "! You take " + str(Edamage) + " damage!")
            health = health - Edamage

    if health > 0:
        print("You win! Leveled up and gained health increase!")
        health = 100 + 1
        level = level + 1
        return True
    else:
        return False
    time.sleep(3)



def clearScreen():
    clear = lambda: os.system('cls')
    clear()


def hospitalBunker(choice):
    global location
    if playerState.get("start"):
        print("...")
        print("Where am I?")
        print(f"{Fore.LIGHTRED_EX}You open your eyes and see the ceiling. You sit up. What will you do?{Fore.RESET}")
        playerState["start"] = False
    elif choice == "":
        print(f"{Fore.LIGHTBLACK_EX}What will you do?{Fore.RESET}")
    elif choice.find("look") >= 0:
        print(f"{Fore.LIGHTRED_EX}You study your surroundings. It looks like you are in a small dimly-lit room. On "
              f"the floor there is a pamphlet. To your right is an opening to a hallway that seems to go on forever.{Fore.RESET}")
    elif choice.find("pamphlet") >= 0:
        print(f"{Fore.LIGHTRED_EX}You pick up the news pamphlet. It reads...")
        print(f"{Fore.BLUE}Local occult group threatens to 'destroy the world' with mysterious artifact. Rumors of "
              f"mayor being leader of mysterious satanist group circle as elections approach.{Fore.RESET}")
        inventory.append("pamphlet")
    elif choice.find("walk") >= 0 or choice.find("hallway") >= 0 or choice.find("right") >= 0:
        print(f"{Fore.LIGHTRED_EX}You walk out of the bunker room{Fore.RESET}")
        location = "hospitalHallway"
        playerState["start"] = True
    else:
        print(f"{Fore.LIGHTBLACK_EX}I do not understand{Fore.RESET}")


def hospitalHallway(choice):
    global location
    if playerState.get("start") or choice.find("look") >= 0:
        print(
            f"{Fore.LIGHTRED_EX}As you walk through the hallway, you hear strange sounds in the distance. You reach a "
            f"crossroad: To your left is another hallway. To your right is a door.")
        print(f"What will you do?{Fore.RESET}")
        playerState["start"] = False
    if choice.find("door") >= 0 or choice.find("right") >= 0:
        print(f"{Fore.RED}You sense a terrifying presence behind this door. Do you wish to continue?{Fore.RESET}")
        playerState["door"] = True
    elif choice.find("yes") >= 0 and playerState.get("door") == True:
        print(f"{Fore.RED}Behind the door, there is a demon with fangs. You could not get away in time...{Fore.RESET}")
        playerState["end"] = True
    elif choice.find("left") >= 0 or choice.find("hallway") >= 0 or (choice.find("no") >= 0 and playerState.get("door") ==True):
        print(f"{Fore.RED}You continue walking down the path. Strange noises can continue being heard...{Fore.RESET}")
        location = "hospitalLobby"
        playerState["start"] = True
    elif choice == "":
        print("")
    else:
        print("I do not understand")


def hospitalLobby(choice):
    global location
    if playerState.get("start"):
        print(f"{Fore.LIGHTRED_EX}You walk into a large room. It looks like an earthquake had happened, as pieces of "
              f"the ceiling are on the ground. It becomes apparent where you are.{Fore.RESET}")
        time.sleep(3)
        print("I'm in a hospital")
        time.sleep(3)
        print(f"{Fore.LIGHTRED_EX}There is a shattered mirror to the right. To the left, it looks like there is a "
              f"strange object. The exit is straight forward{Fore.RESET}")
        print(f"{Fore.LIGHTRED_EX}What will you do?{Fore.RESET}")
        playerState["start"] = False
    if choice.find("right") >= 0 or choice.find("mirror") >= 0:
        print(
            f"{Fore.LIGHTRED_EX}You see your reflection in the mirror. You are bearing strange tattoos...{Fore.RESET}")
    elif choice.find("left") >= 0 or choice.find("object") >= 0:
        print(f"{Fore.LIGHTRED_EX}The artifact is a sword! You pick up the weapon{Fore.RESET}")
        print("Whats a sword doing in a hospital?")
        inventory.append("Sword")
    elif choice.find("straight") >= 0 or choice.find("leave") >= 0 or choice.find("exit") >= 0:
        print(f"{Fore.GREEN}NOT SO FAST!{Fore.RESET}")
        time.sleep(3)
        print("A strange creature with wings emerges from the darkness.")
        print(f"{Fore.GREEN}I CHALLENGE YOU TO A DUEL! LET'S SEE WHO'S THE STRONGEST AROUND HERE!")
        time.sleep(3)
        print(f"{Fore.BLUE}You have engaged in combat{Fore.RESET}")
        time.sleep(3)
        if combat("Fanged Foe", 20, "strike", 1) == True:
            print(f"{Fore.LIGHTRED_EX}You leave the hospital{Fore.RESET}")
            location = "open world"
            playerState["start"] = True
        else:
            playerState["end"] = True


def openWorld(choice):
    global location
    if playerState.get("start"):
        print(f"{Fore.LIGHTRED_EX}You step outside and see the barren wasteland left behind. The sky is red and all "
              f"that's left of what used to be around the hospital has all but been trend to dust. To your right in "
              f"the distance is the city. To your left is an old temple. Strange noises continue to be heard. {Fore.RESET}")
        print("Demons, this place is crawling with them. I need to find someone.")
        playerState["start"] = False
    print(f"{Fore.LIGHTRED_EX}Where will you go?{Fore.RESET}")
    if choice.find("right") >= 0 or choice.find("city") >= 0:
        print(f"{Fore.LIGHTRED_EX}You have decided to go to the city{Fore.RESET}")
        location = "city"
    elif choice.find("left") >= 0 or choice.find("temple") >= 0:
        print(f"{Fore.LIGHTRED_EX}You have decided to go to the temple{Fore.RESET}")
        location = "temple"
    elif choice == "":
        print()
    else:
        print("We need to do something...")


def temple(choice):
    print()

def city(choice):
    print(f"{Fore.LIGHTRED_EX}The city is in ruins. You look around. To the right is something shiny. To the left is "
          f"another area. Straight ahead, there seems to be an entrance to the underground mall{Fore.RESET}")

# Start of Program
print(f"{Fore.BLACK}...{Fore.RESET}")
inventory.append("Fists")
clearScreen()
while not playerState.get("end"):
    if location == "hospitalBunker":
        hospitalBunker(choice)
    elif location == "hospitalHallway":
        hospitalHallway(choice)
    elif location == "hospitalLobby":
        hospitalLobby(choice)
    elif location == "open world":
        openWorld(choice)
    elif location == "temple":
        temple(choice)
    elif location == "city":
        city(choice)
    choice = input("Enter command: ")
    choice = choice.lower()
    clearScreen()

print("GAME OVER")
