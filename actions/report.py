def build_facility_report(arboretum):
    line_width = 20
    for river in arboretum.rivers:
        print(f'River [{river.id}]')
        for animal in river.animals:
            print(f'    ' + animal.species,f'({animal.id})')
    for coastline in arboretum.coastlines:
        print(f'Coastline [{coastline.id}] [{coastline.animals}]')



    input("\n\nPress any key to continue...")