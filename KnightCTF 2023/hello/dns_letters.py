import base64


with open('dns_names_uniq.txt', 'r') as f:
    file = f.readlines()
    flag_base64 = ''
    for i in file:
        i = i.strip("\n").strip()
        if len(i) > 14:
            flag_i = i.split('.')
            flag_base64 += flag_i[0]

print(flag_base64)

flag_base64 = "V" + flag_base64 + "="
print(flag_base64)

flag = base64.b64decode(flag_base64.encode('ascii')).decode('ascii')
print(flag)