import os
import time
from colorama import Fore
from colorama import Style
from colorama import Back
import random

# story: awake in hospital
playerLevel = 1
health = 100
choice = ""
attack = ""
playerState = {"start": True,
               "end": False,
               "door": False,
               "city": False,
               "temple": False,
               "mall key": False}

inventory = []
location = "hospitalBunker"



def findItem(item):
    for i in range(len(inventory)):
        if i == item:
            return True
    return False

def combat(enemy, Ehealth, Eattack, lvl) :
    global health
    global attack
    global playerLevel
    while Ehealth > 0 and health > 0:
        print("Inventory: " + str(inventory))
        if findItem("Book of Spells"):
            print("Spells: Fire Spell, Poison Spell, Healing Spell")
        attack = input("What attack will you use? ")
        attack.lower()
        print()
        if attack.find("sword") >= 0 and findItem("sword"):
            damage = random.choice([2,3,4,5,6,7,8,9,10] * playerLevel)
            print("You swung your sword and do " + str(damage) + " damage!")
        elif attack.find("fist") >= 0:
            damage = random.choice([1,2,3,4,5] * playerLevel)
            print("You go for a punch and do " + str(damage) + " damage")
        elif attack.find("axe") >= 0 and findItem("axe"):
            damage = random.choice([6, 8, 10]) * playerLevel
            print("You swing the mighty axe and do " + str(damage) + " damage")
        elif attack.find("Fire") >= 0 and findItem("Book of Spells") == True:
            damage = random.choice([3, 5, 7, 9]) * playerLevel
            print("You conjure a fireball and do " + str(damage) + " damage")
        elif attack.find("poison") >= 0 and findItem("Book of Spells") == True:
            numAttck = random.choice([1,2,3,4])
            damage = random.choice([1,2,3,4,5])
            damage = numAttck * damage
            print("You struck with posion darts " + str(numAttck) + " times and did " + str(damage) + " total damage!")
        elif attack.find("Healing") >= 0 and findItem("Book of Spells") == True:
            healthGained = random.choice([1,2,3,4]) * playerLevel
            print("You gained " + str(healthGained) + " health")
            health = health + healthGained
        Ehealth = Ehealth - damage
        if Ehealth > 0:
            Edamage = random.choice([1, 2, 3, 4, 5]) * lvl
            print(str(enemy) + " strikes and uses " + str(Eattack) + "! You take " + str(Edamage) + " damage!")
            health = health - Edamage

    if health > 0:
        print(f"{Fore.GREEN}You win! Leveled up and gained health increase!{Fore.RESET}")
        health = 100 + 1
        playerLevel = playerLevel + 1
        return True
    else:
        return False



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
        print("[look around]")
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
        print("[Press Enter]")
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
        print("[Left]   [Right]    ")
    if choice.find("door") >= 0 or choice.find("right") >= 0:
        print(f"{Fore.RED}You sense a terrifying presence behind this door. Do you wish to continue?{Fore.RESET}")
        playerState["door"] = True
    elif choice.find("yes") >= 0 and playerState.get("door") == True:
        print(f"{Fore.RED}Behind the door, there is a demon with fangs.{Fore.RESET}")
        print(f"{Fore.BLUE}You have engaged in combat{Fore.RESET}")
        combat("Baphomet", 500, "Dark Fang", 10)
        if combat("Baphomet", 500, "Dark Fang", 10) == False:
            playerState["end"] = True
    elif choice.find("left") >= 0 or choice.find("hallway") >= 0 or (choice.find("no") >= 0 and playerState.get("door") ==True):
        print(f"{Fore.RED}You continue walking down the path. Strange noises can continue being heard...{Fore.RESET}")
        print("[Press Enter]")
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
              f"strange object. The exit is straight ahead{Fore.RESET}")
        print(f"{Fore.LIGHTRED_EX}What will you do?{Fore.RESET}")
        print("[Right] [Left] ")
        playerState["start"] = False
    if choice.find("right") >= 0 or choice.find("mirror") >= 0:
        print(f"{Fore.LIGHTRED_EX}You see your reflection in the mirror. You are bearing strange tattoos...{Fore.RESET}")
        print("[Left] [Exit]")
    elif choice.find("left") >= 0 or choice.find("object") >= 0:
        print(f"{Fore.LIGHTRED_EX}The artifact is a sword! You pick up the weapon{Fore.RESET}")
        print("Whats a sword doing in a hospital?")
        print("[Exit]")
        inventory.append("sword")
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
            print("[Press Enter]")
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
    print(f"{Fore.LIGHTRED_EX}Your are in the open world. Where will you go?{Fore.RESET}")
    if choice.find("right") >= 0 or choice.find("city") >= 0:
        print(f"{Fore.LIGHTRED_EX}You have decided to go to the city{Fore.RESET}")
        location = "city"
        print("[Press Enter]")
    elif choice.find("left") >= 0 or choice.find("temple") >= 0:
        print(f"{Fore.LIGHTRED_EX}You have decided to go to the temple{Fore.RESET}")
        location = "temple"
        print("[Press Enter]")
    elif choice == "":
        print()
    else:
        print("We need to do something...")


def temple(choice):
    global location
    if playerState.get("temple") == False:
        print(f"{Fore.LIGHTRED_EX}The temple is in ruins...{Fore.RESET}")
        time.sleep(3)
        print(f"{Fore.RED}You sense a terrifying presence inside the temple. Will you head inside?{Fore.RESET}")
        playerState["temple"] = True;
    if choice.find("yes") >= 0:
        print(f"{Fore.RED}You've come face to face with another demon beast{Fore.RESET}")
        print(f"{Fore.BLUE}You have engaged in combat{Fore.RESET}")
        time.sleep(3)
        combat("Titanomachia", 50, "Vicious Strike", 3)
        if combat("Titanomachia", 50, "Vicious Strike", 3) == True:
            print(f"{Fore.LIGHTRED_EX}You have defeated the beast. Inside the temple is a silent atmosphere. A single {Fore.GREEN}altar{Fore.LIGHTRED_EX} sits alone.{Fore.RESET}")
            if choice.find("altar") >= 0:
                print(f"{Fore.LIGHTRED_EX}You search the altar and find a {Fore.CYAN}Book of Spells{Fore.LIGHTRED_EX}")
                inventory.append("Book of Spells")
            else:
                print("")
        else:
            playerState["end"] = True
    if choice.find("leave") >= 0 or choice.find("exit") >= 0:
        location = "open world"
        print(f"{Fore.LIGHTRED_EX}You left the temple{Fore.RESET}")



def city(choice):
    global location
    if playerState.get("city") == False:
        print(f"{Fore.LIGHTRED_EX}The city is in ruins. You look around. To the right is something shiny. To the left "
              f"is another area. Straight ahead, there seems to be an entrance to the underground mall{Fore.RESET}")
    print(f"{Fore.LIGHTRED_EX}What will you do?{Fore.RESET}")
    if choice.find("right") >= 0:
        print(f"{Fore.LIGHTRED_EX}You search and find a {Fore.GREEN}Nordic Axe{Fore.LIGHTRED_EX}!")
        inventory.append("Axe")
    elif choice.find("left") >= 0:
        print(f"{Fore.LIGHTRED_EX}You moved to a secluded spot. There is loose {Fore.GREEN}rubble{Fore.LIGHTRED_EX} in the side of a fallen buidling{Fore.RESET}")
    elif choice.find("rubble") >= 0:
        print(f"{Fore.LIGHTRED_EX}You find a special shaped key. {Fore.RESET}")
        playerState["mall key"] = True
    elif choice.find("go back") >= 0:
        print(f"{Fore.LIGHTRED_EX}You are back in the main area of the city.{Fore.RESET}")
    elif choice.find("go underground") >= 0:
        if playerState.get("mall key") == True:
            print(f"{Fore.LIGHTRED_EX}You open the door to find that there are enemies lined up in sequential order. "
                  f"You must take them down{Fore.RESET}")
            time.sleep(3)
            print(f"{Fore.BLUE}You have engaged in combat{Fore.RESET}")
            combat("Pyro Jack", 25, "Slash", 2)
            if combat("Pyro Jack", 25, "Slash", 2):
                print()
                time.sleep(3)
                print(f"{Fore.BLUE}You have engaged in combat{Fore.RESET}")
                combat("Jack Frost", 35, "Frostbite", 2)
                if combat("Jack Frost", 35, "Frostbite", 2):
                    print()
                    time.sleep(3)
                    print(f"{Fore.LIGHTRED_EX}The final enemy shows itself{Fore.RESET}")
                    print(f"{Fore.BLUE}You have engaged in combat{Fore.RESET}")
                    combat("King Jack", 150, "Final Order", 7)
                    if combat("King Jack", 150, "Final Order", 7):
                        print(f"{Fore.LIGHTRED_EX}After the long battle, an item was dropped:")
                        print(f"{Fore.LIGHTRED_EX}You found a {Fore.GREEN}chalice of the underworld{Fore.RESET}")
                        print(f"{Fore.LIGHTRED_EX}Leave city?{Fore.RESET}")
                        if choice.find("Yes") >= 0:
                            print(f"{Fore.LIGHTRED_EX}You have left the city{Fore.RESET}")
                            location = "open world"
                        else:
                            print("")
        else:
            print("I need some sort of key...")








# Start of Program
print(f"{Fore.BLACK}...{Fore.RESET}")
inventory.append("fists")
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

print("''Death is not the end.....''")
print("GAME OVER")
