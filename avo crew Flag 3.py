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
    list_of_keys = list(keys1) 
    
    for key in keys2:
        if key not in list_of_keys:
            list_of_keys.append(key)

    for key in list_of_keys:
        if key in keys1 and key in keys2:
            merged_list = spellbook1[key]

            for spell in spellbook2[key]:
                if spell not in merged_list:
                    merged_list.append(spell)
                    
            merged[key] = merged_list
                
        elif key in keys1:
            merged[key] = spellbook1[key]
        elif key in keys2:
            merged[key] = spellbook2[key]
        
    return merged

merged = spellbook(spellbook1,spellbook2)
print(merged)