def build_facility_report(arboretum):

    for mountain in arboretum.mountains:
        print(f'Mountain [{"%.8s" % mountain.id}]')
        for animal in mountain.animals:
            print(f'      {animal.species} ({"%.8s" % animal.id})')
        for plant in mountain.plants:
            print(f'      {plant.species} ({"%.8s" % plant.id})')

    for grassland in arboretum.grasslands:
        print(f'\nGrassland [{"%.8s" % grassland.id}]')
        for animal in grassland.animals:
            print(f'      {animal.species} ({"%.8s" % animal.id})')
        for plant in grassland.plants:
            print(f'      {plant.species} ({"%.8s" % plant.id})')

    for river in arboretum.rivers:
        print(f'\nRiver [{"%.8s" % river.id}]')
        for animal in river.animals:
            print(f'      {animal.species} ({"%.8s" % animal.id})')
        for plant in river.plants:
            print(f'      {plant.species} ({"%.8s" % plant.id})')

    for forest in arboretum.forests:
        print(f'\nForest [{"%.8s" % forest.id}]')
        for animal in forest.animals:
            print(f'     {animal.species} ({"%.8s" % animal.id})')
        for plant in forest.plants:
            print(f'      {plant.species} ({"%.8s" % plant.id})')

    for swamp in arboretum.swamps:
        print(f'\nSwamp [{"%.8s" % swamp.id}]')
        for animal in swamp.animals:
            print(f'     {animal.species} ({"%.8s" % animal.id})')
        for plant in swamp.plants:
            print(f'      {plant.species} ({"%.8s" % plant.id})')

    for coastline in arboretum.coastlines:
        print(f'\nCoastline [{"%.8s" % coastline.id}]')
        for animal in coastline.animals:
            print(f'     {animal.species} ({"%.8s" % animal.id})')
        for plant in coastline.plants:
            print(f'      {plant.species} ({"%.8s" % plant.id})')

    input("\n\nPress any key to continue...")