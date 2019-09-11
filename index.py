import os
from arboretum import Arboretum
from actions.release_animal import release_animal
from actions.cultivate_plant import cultivate_plant
from actions.feed_animal import feed_animal
from actions.annex import annex_habitat
from actions.report import build_facility_report

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ \n \033[1;31;40m|  \033[1;37;40mK  e  a  h  u  a    A  r  b  o  r  e  t  u  m  \033[1;31;40m| \n \033[1;37;40m+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("")
    print("1. Annex Biome")
    print("2. Release New Animal")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Show Arboretum Report")
    print("6. Exit")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input("\n Choose a KILLER option \n \033[1;31;40m> \033[1;37;40m")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        feed_animal(keahua)

    if choice == "4":
        cultivate_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)


    if choice != "6":
        main_menu()

main_menu()
