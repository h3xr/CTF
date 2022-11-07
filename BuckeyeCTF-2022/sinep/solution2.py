import string
from pwn import *

goal_string = "0x111c0d0e150a0c151743053607502f1e10311544465c5f551e0e"
input_string = ""

while True:
    for i in string.printable:

        p = process(["./sinep.sh", f"{input_string + i}"])
        p.recvuntil("Final: ")

        hex_output = p.recvline().decode().strip()

        if hex_output == goal_string:
                    print(f"The flag is: {input_string}")
                    exit()
        p.close()
        if hex_output in goal_string:
                print("Eureka!")
                input_string += i
                print(input_string)
                break