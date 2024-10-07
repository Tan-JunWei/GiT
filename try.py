spellbook1 = { "Elemental Magic":["Fireball", "Lightning Bolt","Earthquake"], 
              "Healing Magic": ["Heal", "GreaterHeal"], 
              "Dark Magic":["Curse"] }
spellbook2 = { "Elemental Magic":["Fireball", "Ice Storm"],
              "Healing Magic": ["Heal"],
              "Necromancy": ["RaiseUndead", "Life Drain"] }
merged_spellbook = {}

for key1 in spellbook1:
    for key2 in spellbook2:
        if key1 == key2:
            l1 = spellbook1[key1]
            l2 = spellbook2[key2]
            for spell in l1:
                if spell in l2:
                    l2.pop(l2.index(spell))
            l1 += l2
            merged_spellbook[key1] = l1
        else:
            merged_spellbook[key2] = spellbook2[key2]

print(merged_spellbook)
