from animals import RiverDolphin

def release_plant(arboretum):
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

        for index, forest in enumerate(arboretum.forests):
            print(f'{index + 1}. Forest {forest.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.forests[int(choice) - 1].animals.append(animal)

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


        for index, biome in enumerate(new_list):
            print(f'{index + 1}. {biome["type"]} ({len(biome["animals"])} animals) ')

        print("Where would you like to place the animal?")
        choice = input("> ")
        choice = new_list[int(choice) - 1]

        if choice["type"] == "River":
            if len(choice["animals"]) < choice["animal_max"]:
                arboretum.rivers[int(choice["index"])].add_animal((animal))
            else:
                print("NOOOO")
                input("Press any key to continue")
                for index, biome in enumerate(new_list):
                    print(f'{index + 1}. {biome["type"]} ({len(biome["animals"])} animals) ')

                print("Where would you like to place the animal?")
                choice = input("> ")
                choice = new_list[int(choice) - 1]
                arboretum.rivers[int(choice["index"])].add_animal((animal))
        else:
            arboretum.coastlines[int(choice["index"])].animals.append(animal)



    if choice == "3":
        animal = NeneGoose()

        for index, grassland in enumerate(arboretum.grasslands):
            print(f'{index + 1}. Grassland {grassland.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.grasslands[int(choice) - 1].animals.append(animal)

    if choice == "4":
        animal = Kikakapu()
        # biome  river/swamp
        for index, river in enumerate(arboretum.rivers):
            print(f'{index + 1}. River {river.id}')

        for index, swamp in enumerate(arboretum.swamps):
            print(f'{index + 1}. Swamp {swamp.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.swamps[int(choice) - 1].animals.append(animal)

    if choice == "5":
        animal = Pueo()
        # biome =  grassland/forest
        for index, grassland in enumerate(arboretum.grasslands):
            print(f'{index + 1}. Grassland {grassland.id}')

        for index, forest in enumerate(arboretum.forests):
            print(f'{index + 1}. Forest {forest.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.grasslands[int(choice) - 1].animals.append(animal)

    if choice == "6":
        animal = Ulae()

        for index, coastline in enumerate(arboretum.coastlines):
            print(f'{index + 1}. Coastline {coastline.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.coastlines[int(choice) - 1].animals.append(animal)

    if choice == "7":
        animal = Opeapea()
        # biome = forest/mountain
        for index, forest in enumerate(arboretum.forests):
            print(f'{index + 1}. Forest {forest.id}')

        for index, mountain in enumerate(arboretum.mountains):
            print(f'{index + 1}. Mountain {mountain.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.forests[int(choice) - 1].animals.append(animal)

    if choice == "8":
        animal = HappyFaceSpider()

        for index, swamp in enumerate(arboretum.swamps):
            print(f'{index + 1}. Swamp {swamp.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.swamps[int(choice) - 1].animals.append(animal)




