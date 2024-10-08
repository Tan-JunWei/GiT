artifacts = [
    (1, 10, 2),
    (2, 20, 3),
    (3, 15, 1),
    (4, 30, 4),
    (5, 25, 2)
]

max_weight = 6
artifacts_id = ""
magic_points = 0    

for i in range(len(artifacts)):

    for k in range(i+1, len(artifacts)):
        total_weight = artifacts[i][2] + artifacts[k][2]
        sum = artifacts[i][1] + artifacts[k][1]

        if total_weight <= max_weight and sum > magic_points:
            magic_points = sum
            artifacts_id = str(artifacts[i][0]) + str(artifacts[k][0])
            print(f"Magic points: {magic_points}")
            print(f"Total weight of artifacts: {total_weight}")
            print(f"ID: {artifacts_id}\n")

print(f"Maximum magic points: {magic_points}")
print(f"Best ID: {artifacts_id}")