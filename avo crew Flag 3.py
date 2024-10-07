spellbook1 = { "Elemental Magic":["Fireball", "Lightning Bolt","Earthquake"], 
              "Healing Magic": ["Heal", "GreaterHeal"], 
              "Dark Magic":["Curse"] }
spellbook2 = { "Elemental Magic":["Fireball", "Ice Storm"],
              "Healing Magic": ["Heal"],
              "Necromancy": ["RaiseUndead", "Life Drain"] }

def spellbook(spellbook1,spellbook2):
    merged = {}
    keys1 = spellbook1.keys()
    keys2 = spellbook2.keys()
    list_of_keys = list(keys1) + list(keys2)

    for key in keys1:
        if key in keys2:
            list_of_keys.remove(key)

    for key in list_of_keys:

        if key in keys1 and key in keys2:
            merged[key] = spellbook1[key] + spellbook2[key]
            for key in merged.keys():
                value = merged[key]
                for i in value:
                    if value.count(i) > 1:
                        value.remove(i)
                
        elif key in keys1:
            merged[key] = spellbook1[key]
        elif key in keys2:
            merged[key] = spellbook2[key]
        
    return merged

merged = spellbook(spellbook1,spellbook2)
print(merged)