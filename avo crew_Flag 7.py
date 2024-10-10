spells = {"spells": 
          {"fireball": {"description": "Burns with the fury of a thousand suns", "power": "High"},
           "lightning": {"description": "Strikes with the speed of thunder", "power": "Medium"},
            "bolt": {"description": "A quick and sharp surge", "power": "Low"}},
        "common_spells": {"rays": {"description": "A blazing inferno","power": "High"},
                        "explosion": {"description": "A sudden burst","power": "Low"}}}

encrypted_message = "fireball lightning bolt rays explosion"
encrypted_list = encrypted_message.split()
decrypted = ""

for spell_name in encrypted_list:
    if spell_name in spells["spells"]:
        decrypted += f"{spells["spells"][spell_name]['description']} "

    elif spell_name in spells["common_spells"]:
        decrypted += f"{spells['common_spells'][spell_name]['power']} " 
        
    else:
        continue
        
print(decrypted)