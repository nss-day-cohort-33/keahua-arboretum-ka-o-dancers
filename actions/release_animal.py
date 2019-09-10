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
    return False


def release_animal(arboretum):
    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = DayGecko()
        new_list = []      
        if len(arboretum.forests) > 0:
            for index, forest in enumerate(arboretum.forests):
                new_list.append({"index": index,
                                  "id": forest.id,
                                  "type": "Forest",
                                  "animals": forest.animals,
                                  "animal_max": forest.animal_max
                                })
        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

        if choice["type"] == "Forest" and valid:
            arboretum.forests[int(choice["index"])].add_animal((animal))


    if choice == "2":
        animal = RiverDolphin()
        new_list = []


        if len(arboretum.rivers) > 0:
            for index, river in enumerate(arboretum.rivers):
                new_list.append({"index": index,
                                  "id": river.id,
                                  "type": "River",
                                  "animals": river.animals,
                                  "animal_max": river.animal_max
                                })


        if len(arboretum.coastlines) > 0:
            for index, coastline in enumerate(arboretum.coastlines):
                new_list.append({"index": index,
                                  "id": coastline.id,
                                  "type": "Coastline",
                                  "animals": coastline.animals,
                                  "animal_max": coastline.animal_max
                                })

        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

        if choice["type"] == "River" and valid:
            arboretum.rivers[int(choice["index"])].add_animal((animal))

        elif choice["type"] == "Coastline" and valid:
            arboretum.coastlines[int(choice["index"])].add_animal((animal))



    if choice == "3":
        animal = NeneGoose()
        new_list = []      
        if len(arboretum.grasslands) > 0:
            for index, grassland in enumerate(arboretum.grasslands):
                new_list.append({"index": index,
                                  "id": grassland.id,
                                  "type": "Grassland",
                                  "animals": grassland.animals,
                                  "animal_max": grassland.animal_max
                                })
        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

        if choice["type"] == "Grassland" and valid:
            arboretum.grasslands[int(choice["index"])].add_animal((animal))

    if choice == "4":
        animal = Kikakapu()
        new_list = []


        if len(arboretum.rivers) > 0:
            for index, river in enumerate(arboretum.rivers):
                new_list.append({"index": index,
                                  "id": river.id,
                                  "type": "River",
                                  "animals": river.animals,
                                  "animal_max": river.animal_max
                                })


        if len(arboretum.swamps) > 0:
            for index, swamp in enumerate(arboretum.swamps):
                new_list.append({"index": index,
                                  "id": swamp.id,
                                  "type": "Swamp",
                                  "animals": swamp.animals,
                                  "animal_max": swamp.animal_max
                                })

        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

        if choice["type"] == "River" and valid:
            arboretum.rivers[int(choice["index"])].add_animal((animal))

        elif choice["type"] == "Swamp" and valid:
            arboretum.swamps[int(choice["index"])].add_animal((animal))

    if choice == "5":
        animal = Pueo()
        new_list = []


        if len(arboretum.grasslands) > 0:
            for index, grassland in enumerate(arboretum.grasslands):
                new_list.append({"index": index,
                                  "id": grassland.id,
                                  "type": "Grassland",
                                  "animals": grassland.animals,
                                  "animal_max": grassland.animal_max
                                })


        if len(arboretum.forests) > 0:
            for index, forest in enumerate(arboretum.forests):
                new_list.append({"index": index,
                                  "id": forest.id,
                                  "type": "Forest",
                                  "animals": forest.animals,
                                  "animal_max": forest.animal_max
                                })
        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

        if choice["type"] == "Grassland" and valid:
            arboretum.grasslands[int(choice["index"])].add_animal((animal))

        elif choice["type"] == "Forest" and valid:
            arboretum.forests[int(choice["index"])].add_animal((animal))
    if choice == "6":
        animal = Ulae()
        new_list = []      
        if len(arboretum.coastlines) > 0:
            for index, coastline in enumerate(arboretum.coastlines):
                new_list.append({"index": index,
                                  "id": coastline.id,
                                  "type": "Coastline",
                                  "animals": coastline.animals,
                                  "animal_max": coastline.animal_max
                                })
        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

        if choice["type"] == "Coastline" and valid:
            arboretum.coastlines[int(choice["index"])].add_animal((animal))

    if choice == "7":
        animal = Opeapea()
        new_list = []

        if len(arboretum.forests) > 0:
            for index, forest in enumerate(arboretum.forests):
                new_list.append({"index": index,
                                  "id": forest.id,
                                  "type": "Forest",
                                  "animals": forest.animals,
                                  "animal_max": forest.animal_max
                                })


        if len(arboretum.mountains) > 0:
            for index, mountain in enumerate(arboretum.mountains):
                new_list.append({"index": index,
                                  "id": mountain.id,
                                  "type": "Mountain",
                                  "animals": mountain.animals,
                                  "animal_max": mountain.animal_max
                                })
        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

        if choice["type"] == "Forest" and valid:
            arboretum.forests[int(choice["index"])].add_animal((animal))

        elif choice["type"] == "Mountain" and valid:
            arboretum.mountains[int(choice["index"])].add_animal((animal))

    if choice == "8":
        animal = HappyFaceSpider()
        new_list = []      
        if len(arboretum.swamps) > 0:
            for index, swamp in enumerate(arboretum.swamps):
                new_list.append({"index": index,
                                  "id": swamp.id,
                                  "type": "Swamp",
                                  "animals": swamp.animals,
                                  "animal_max": swamp.animal_max
                                })
        valid = False
        while valid == False:
            choice = print_biome(new_list)
            valid = check_capacity(choice)

        if choice["type"] == "Swamp" and valid:
            arboretum.swamps[int(choice["index"])].add_animal((animal))





