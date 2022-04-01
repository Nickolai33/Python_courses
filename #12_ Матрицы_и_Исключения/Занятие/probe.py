sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
distances = {}
sites_copy = sites.copy()
for state, coord in sites.items():
    del sites_copy[state]
    for state_copy, coord_copy in sites_copy.items():
        dva_goroda = state + "-" + state_copy
        rasstoyanie = (coord[0] - coord_copy[0]) ** 2 + (coord[1] - coord_copy[1])
        distances.setdefault(dva_goroda, rasstoyanie)
print(distances)
