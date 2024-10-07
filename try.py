def validate_pin(pin):
    first_digit = str(pin)[0]
    second_digit = str(pin)[1]
    third_digit = str(pin)[2]

    condition1 = pin % 5 == 0 and pin % 7 == 0 # divisible by 5 and 7
    condition2 = int(first_digit) % 2 == 1 # first digit is odd
    condition3 = int(second_digit) % 2 == 1 and second_digit != first_digit # second digit is odd and not equal to first digit
    condition4 = int(third_digit) % 2 == 0 # third digit is even
    condition5 = len(set(str(pin))) == 4 # no repeated digits

    if condition1 and condition2 and condition3 and condition4 and condition5:
        return True
    
count = 1
for i in range(1000,10000):
    if validate_pin(i):
        count +=1
print(count)