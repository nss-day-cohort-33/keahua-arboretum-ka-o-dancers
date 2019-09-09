def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River [{river.id}]')
        for animal in river.animals:
            print(animal.species, animal.id)
    for coastline in arboretum.coastlines:
        print(f'Coastline [{coastline.id}] [{coastline.animals}]')



    input("\n\nPress any key to continue...")