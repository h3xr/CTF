with open("flag.enc.txt", "r") as file:
    flag = file.read()

    for each in flag:
        each = chr(ord(each) ^ 0x66)
        flag += each

print(flag)