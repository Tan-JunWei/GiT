def validate_password():
    accepted = 0
    for pin in range(1000, 10000):
        validate = True
        pin_list = list(str(pin))

        if pin%5 != 0:
            validate = False

        elif pin%7 != 0:
            validate = False

        elif int(pin_list[0]) % 2 == 0:
            validate = False

        elif int(pin_list[1]) % 2 == 0 and pin_list[1] == pin_list[0]:
            validate = False

        elif int(pin_list[2]) % 2 != 0:
            validate = False
        
        for i in pin_list:
            count = pin_list.count(i)
            if count == 1:
                validate = False
            
        if validate == True:
            accepted += 1
        else:
            continue

    return accepted

print(validate_password())