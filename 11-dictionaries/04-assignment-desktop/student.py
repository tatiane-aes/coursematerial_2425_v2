def desktop(catalog, components):
    catalog = {
    'Intel Core i7 13700K': 439,
    'Intel Core i5 13600K': 331}
    components = {
    'Gigabyte Z790 AORUS ELITE AX': 261}

    total_cost = 0
    for component in components:
        total_cost += catalog[component]
    return total_cost

print(desktop(['Intel Core i7 13700K', 'Gigabyte Z790 AORUS ELITE AX']))


# ALGO DEU ERRADO ???? 