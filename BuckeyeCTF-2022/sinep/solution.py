import string

flag_candidates = string.printable
ans = "0x111c0d0e150a0c151743053607502f1e10311544465c5f551e0e"
ans = ans[2:]
flag_list = []
for i in range(0, len(ans), 2):
    flag_list.append(ans[i:i+2])
print(len(flag_list), flag_list)

flag = 'buckeye{'
initial_flag_len = len(flag)
flag = list(flag)
sinep = "sinep"

while len(flag) < len(flag_list):
  for c in flag_candidates:
    flag_is_match = False
    flag_for_concat = flag + [c]
    flag_tmp = flag + [c]
    #print(flag_tmp)
    cnt = 0
    while True:
      if cnt >= len(flag_tmp):
        break
      index = cnt
      char_input = (ord(sinep[cnt % 5])) ^ ord(flag_tmp[cnt])
      flag_tmp[index] = chr(char_input)
      cnt += 1
    for i,j in enumerate(flag_tmp):
      res = '{:02x}'.format(ord(j))
      if flag_list[i] == res and i == len(flag_tmp) - 1:
        flag_is_match = True
        break
    if flag_is_match:
      print("match!")
      flag = flag_for_concat
      break

print("".join(flag))