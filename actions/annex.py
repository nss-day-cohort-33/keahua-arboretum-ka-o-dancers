import os
from environments import River

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")

    choice = input("Choose your habitat > ")

    if choice == "5":
        river = River()
        arboretum.rivers.append(river)


    if choice == "2":
        pass
