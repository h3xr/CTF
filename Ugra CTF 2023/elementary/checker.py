import base64
import hashlib
import sys


def abort():
    print("Wrong flag!")
    sys.exit(1)


flag = input()

if len(flag) != 29:
    abort()
if flag[17] != 'g':
    abort()
if flag[:5] != 'ugra_':
    abort()
if flag[9:3:-2] != 'nta':
    abort()
if flag[-2:-15:-3].encode().hex() != '786b737567':
    abort()
if int.from_bytes(flag[6:18:2].encode(), "little") != 104927802781555:
    abort()
if sum(ord(x) * 1000 ** i for i, x in enumerate(flag[19:-4])) != 107056052115119102:
    abort()
if base64.b64encode(flag[-4:].encode()) != b'OW14cg==':
    abort()
if hashlib.sha256(flag.encode()).hexdigest() != 'c03d442919809592c613752762555c6cd46c5d39b5ba8dbfaf4c617533b28bb7':
    abort()

print("OK!")
