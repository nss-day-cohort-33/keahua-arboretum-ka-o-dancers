from plants import MountainTree
from plants import Silversword
from plants import RainbowTree
from plants import BlueVine


def print_biome(new_list):
    for index, biome in enumerate(new_list):
        print(f'{index + 1}. {biome["type"]} ({len(biome["plants"])} plants) ')

    print("Where would you like to place the plant?")
    choice = input("> ")
    choice = new_list[int(choice) - 1]
    return choice



def check_capacity(choice):
    if len(choice["plants"]) < choice["plant_max"]:
        return True
    else:
        print("**** That biome is not large enought ****")
        print("**** Please choose another one ****")
    return False



def cultivate_plant(arboretum):
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    choice = input("Choose plant to cultivate > ")

    if choice == "1":
        plant = MountainTree()
        new_list = []

        if len(arboretum.mountains) > 0:
                for index, mountain in enumerate(arboretum.mountains):
                    new_list.append({"index": index,
                                    "id": mountain.id,
                                    "type": "Mountain",
                                    "plants": mountain.plants,
                                    "plant_max": mountain.plant_max
                                    })


        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

            if choice["type"] == "Mountain" and valid:
                arboretum.mountains[int(choice["index"])].add_plant((plant))



    if choice == "2":
        plant = Silversword()
        new_list = []

        if len(arboretum.grasslands) > 0:
                    for index, grassland in enumerate(arboretum.grasslands):
                        new_list.append({"index": index,
                                        "id": grassland.id,
                                        "type": "Grassland",
                                        "plants": grassland.plants,
                                        "plant_max": grassland.plant_max
                                        })


        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

            if choice["type"] == "Grassland" and valid:
                arboretum.grasslands[int(choice["index"])].add_plant((plant))


    if choice == "3":
        plant = RainbowTree()
        new_list = []

        if len(arboretum.forests) > 0:
                    for index, forest in enumerate(arboretum.forests):
                        new_list.append({"index": index,
                                        "id": forest.id,
                                        "type": "Forest",
                                        "plants": forest.plants,
                                        "plant_max": forest.plant_max
                                        })


        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

            if choice["type"] == "Forest" and valid:
                arboretum.forests[int(choice["index"])].add_plant((plant))


    if choice == "4":
        plant = BlueVine()
        new_list = []

        if len(arboretum.grasslands) > 0:
                for index, grassland in enumerate(arboretum.grasslands):
                    new_list.append({"index": index,
                                    "id": grassland.id,
                                    "type": "Grassland",
                                    "plants": grassland.plants,
                                    "plant_max": grassland.plant_max
                                    })


        if len(arboretum.swamps) > 0:
            for index, swamp in enumerate(arboretum.swamps):
                new_list.append({"index": index,
                                    "id": swamp.id,
                                    "type": "Swamp",
                                    "plants": swamp.plants,
                                    "plant_max": swamp.plant_max
                                })

        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

        if choice["type"] == "Grassland" and valid:
            arboretum.grasslands[int(choice["index"])].add_plant((plant))

        elif choice["type"] == "Swamp" and valid:
            arboretum.swamps[int(choice["index"])].add_plant((plant))

