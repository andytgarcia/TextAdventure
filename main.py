import os
import time
from colorama import Fore
from colorama import Style
from colorama import Back

# story: awake in hospital
health = 100
choice = ""
playerState = {"start": True,
               "end": False,
               "door": False}

inventory = []
location = "hospitalBunker"



def combat(enemy, health, attack) :
    while int > 0 or health > 0:
        attack = input("What attack will you use")
        print(inventory)



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
    elif choice.find("left") >= 0 or choice.find("hallway") >= 0:
        print(f"{Fore.RED}You continue walking down the path. Strange noises can continue being heard...{Fore.RESET}")
        location = "hospitalLobby"
        playerState["start"] = True
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
    elif choice.find("straight") >= 0 or choice.find("leave") >= 0 or choice.find("exit") >= 0:
        print(f"{Fore.GREEN}NOT SO FAST!{Fore.RESET}")
        time.sleep(3)
        print("A strange creature with wings emerges from the darkness.")
        print(f"{Fore.GREEN}I CHALLENGE YOU TO A DUEL! LET'S SEE WHO'S THE STRONGEST AROUND HERE!")
        print(f"{Fore.BLUE}You have engaged in combat")
        combat(30)
        print("You leave the hospital")


# Start of Program
print(f"{Fore.BLACK}...{Fore.RESET}")
while not playerState.get("end"):
    if location == "hospitalBunker":
        hospitalBunker(choice)
    elif location == "hospitalHallway":
        hospitalHallway(choice)
    elif location == "hospitalLobby":
        hospitalLobby(choice)
    choice = input("Enter command: ")
    choice = choice.lower()
    clearScreen()

print("GAME OVER")
