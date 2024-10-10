import math
# directions = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]
directions = ["UP 40", "DOWN 2", "LEFT 18", "UP 4", "RIGHT 20", "DOWN 30", "LEFT 5"]
directions_dictionary = {}

for direction in directions:
    direction = direction.split()
    if direction[0] not in directions_dictionary:
        directions_dictionary[direction[0]] = int(direction[1])
    else:
        directions_dictionary[direction[0]] += int(direction[1])

vertical = abs(directions_dictionary["UP"] - directions_dictionary["DOWN"])
horizontal = abs(directions_dictionary["LEFT"] - directions_dictionary["RIGHT"])

distance = math.sqrt(math.pow(vertical,2) + math.pow(horizontal,2)) # a^2 + b^2 = c^2
print(int(distance))
    