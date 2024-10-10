runes = [10, 'cursed', 40, 'broken', 20, 'none', 30, ['trick',20, 30]]
sum = 0
target = 160

for rune in runes:
    try:
        sum += rune

    except TypeError:
        if type(rune) == list:
            for item in rune:
                try:
                    sum += item
                    
                except TypeError:
                    continue

if sum == target:
    print(f"GIT{target}")
else:
    message = f"Failed to decode the rune because the target is now {sum}"
    print(f'GIT{{{message}}}')
