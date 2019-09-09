from animals import RiverDolphin

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

        for index, forest in enumerate(arboretum.forests):
            print(f'{index + 1}. Forest {forest.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.forests[int(choice) - 1].animals.append(animal)

    if choice == "2":
        animal = RiverDolphin()
<<<<<<< HEAD
=======
        num = 0

        if len(arboretum.rivers) > 0:
            for index, river in enumerate(arboretum.rivers):
                print(f'{index + 1}. River {river.id}')
                num = index + 2

        if len(arboretum.coastlines) > 0:
            for index, coastline in enumerate(arboretum.coastlines):
                print(f'{index + num}. Coastline {coastline.id}')


        print("Release the animal into which biome?")
        choice = input("> ")
        if "River" in str:
            arboretum.rivers[int(choice) - 1].animals.append(animal)
        else:
            arboretum.coastlines[int(choice) - num].animals.append(animal)

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
>>>>>>> master
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





