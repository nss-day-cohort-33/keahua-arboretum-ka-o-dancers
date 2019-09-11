from animals import RiverDolphin
from animals import DayGecko
from animals import HappyFaceSpider
from animals import Kikakapu
from animals import NeneGoose
from animals import Pueo
from animals import Ulae
from animals import Opeapea

def print_biome(new_list):
    for index, biome in enumerate(new_list):
        print(f'{index + 1}. {biome["type"]} ({len(biome["animals"])} animals) ')

    print("Where would you like to place the animal?")
    choice = input("> ")
    choice = new_list[int(choice) - 1]
    return choice

def check_capacity(choice):
    if len(choice["animals"]) < choice["animal_max"]:
        return True
    else:
        print("**** That biome is not large enought ****")
        print("**** Please choose another one ****")
    return False

def feed_animal(arboretum):
    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to feed > ")

    if choice == "1":
        animal = DayGecko()

        animal.list_prey()
        choice = input(f'What is on the menu for the {animal.species} today?')

        choice = int(choice) - 1
        choice = animal.prey[choice]
        animal.feed(f"{choice}")
        input("Press any key to continue")


    if choice == "2":
        animal = RiverDolphin()
        animal.list_prey()
        choice = input(f'What is on the menu for the {animal.species} today?')

        choice = int(choice) - 1
        choice = animal.prey[choice]
        animal.feed(f"{choice}")
        input("Press any key to continue")

    if choice == "3":
        animal = NeneGoose()
        animal.list_prey()
        choice = input(f'What is on the menu for the {animal.species} today?')

        choice = int(choice) - 1
        choice = animal.prey[choice]
        animal.feed(f"{choice}")
        input("Press any key to continue")

    if choice == "4":
        animal = Kikakapu()
        animal.list_prey()
        choice = input(f'What is on the menu for the {animal.species} today?')

        choice = int(choice) - 1
        choice = animal.prey[choice]
        animal.feed(f"{choice}")
        input("Press any key to continue")

    if choice == "5":
        animal = Pueo()
        animal.list_prey()
        choice = input(f'What is on the menu for the {animal.species} today?')

        choice = int(choice) - 1
        choice = animal.prey[choice]
        animal.feed(f"{choice}")
        input("Press any key to continue")

    if choice == "6":
        animal = Ulae()
        animal.list_prey()
        choice = input(f'What is on the menu for the {animal.species} today?')

        choice = int(choice) - 1
        choice = animal.prey[choice]
        animal.feed(f"{choice}")
        input("Press any key to continue")

    if choice == "7":
        animal = Opeapea()
        animal.list_prey()
        choice = input(f'What is on the menu for the {animal.species} today?')

        choice = int(choice) - 1
        choice = animal.prey[choice]
        animal.feed(f"{choice}")
        input("Press any key to continue")

    if choice == "8":
        animal = HappyFaceSpider()
        animal.list_prey()
        choice = input(f'What is on the menu for the {animal.species} today?')

        choice = int(choice) - 1
        choice = animal.prey[choice]
        animal.feed(f"{choice}")
        input("Press any key to continue")





