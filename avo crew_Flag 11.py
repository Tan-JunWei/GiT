potion_inventory = {
    "Polyjuice Potion": "Frost Fern",
    "Amortentia": "Fire Lily",
    "Frostbite Elixir": "Phoenix Feather",
    "Elixir of Life": "Aconite Root",
    "Firestarter Potion":"Elderflower"
}

keys = list(potion_inventory.keys())
values = list(potion_inventory.values())

sorted_keys = sorted(keys)
sorted_values = sorted(values)

for i in range(len(sorted_keys)):
    potion_inventory[sorted_keys[i]] = sorted_values[i]

print(sorted(potion_inventory.values()))