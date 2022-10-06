import os
import time
from colorama import Fore
from colorama import Style
from colorama import Back

# story: awake in hospital

choice = ""
playerState = {"start": True,
               "end": False,
               "door": False}

inventory = []
location = "hospitalBunker"


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
    else:
        print(f"{Fore.LIGHTBLACK_EX}I do not understand{Fore.RESET}")


def hospitalHallway(choice):
    print(f"{Fore.LIGHTRED_EX}As you walk through the hallway, you hear strange sounds in the distance. You reach a "
          f"crossroad: To your left is another hallway. To your right is a door.")
    print(f"What will you do?{Fore.RESET}")
    if choice.find("door") >= 0 or choice.find("right") >= 0:
        print(f"{Fore.RED}You sense a terrifying presence behind this door. Do you wish to continue?{Fore.RESET}")
        playerState["door"] = True
    elif choice.find("yes") >= 0 and playerState.get("door") == True:
            print(f"{Fore.RED}Behind the door, there is a demon with fangs. You could not get away in time...{Fore.RESET}")
            playerState["end"] = True


# Start of Program
print(f"{Fore.BLACK}...{Fore.RESET}")
while not playerState.get("end"):
    if location == "hospitalBunker":
        hospitalBunker(choice)
    elif location == "hospitalHallway":
        hospitalHallway(choice)
    choice = input("Enter command: ")
    choice = choice.lower()
    clearScreen()

print("GAME OVER")