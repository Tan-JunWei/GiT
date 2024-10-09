p = 53
q = 97
message = "!L0VEH@RRYP0TTER"
e = 65537
n = p * q

flag = "GIT{"

'''
FORMULA;
c = (m + 1000)^e mod n
'''

for i in range(len(message)):
    ASCII_value = ord(message[i])
    c = pow((ASCII_value + 1000), e, n)
    digits = [int(num) for num in str(c)]
    hash = sum(digits)
    if i != len(message)-1:
        flag += f"{hash}_"
    else:
        flag += f"{hash}}}"

print(flag)
# Flag: GIT{18_20_15_26_8_26_14_21_21_9_15_15_23_23_8_21}