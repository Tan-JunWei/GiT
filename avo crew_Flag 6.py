def sort_crystals_by_power(crystal_powers):
    positive_powers = [p for p in crystal_powers if int(p) >= 0]
    negative_powers = [p for p in crystal_powers if int(p) < 0]

    sorted_powers = sorted(positive_powers, reverse=True)
    final_powers = sorted_powers + negative_powers
    
    return final_powers
    
crystal_powers = ["15", "42", "-9", "33", "57", "-23"]
sorted_crystals = sort_crystals_by_power(crystal_powers)
print(sorted_crystals)