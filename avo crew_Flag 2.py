seats1 = [[1,2,3,4],[3,4,5,6],[7,8,9,10],[11,12,13,14]]
seats2 = [[1,2,3,4],[1,4,5,6],[7,8,9,10],[11,12,13,14]]
enchanted_rows = [1,3]

def can_see_stage(seats, enchanted_rows):
    for i in enchanted_rows:
        for index in range(0,4):
            if seats[i][index] < seats[i-1][index] + 2:
                return False
            else:
                return True
    
print(can_see_stage(seats1, enchanted_rows))
print(can_see_stage(seats2, enchanted_rows))
            