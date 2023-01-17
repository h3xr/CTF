import base64
import hashlib
import sys


def abort():
    print("Wrong flag!")
    sys.exit(1)

# В качестве начального значения примем что:
flag = "0123456789ABCDEFGJHIKLMNOPRST"

# 1
print("Условие: Длина флага 29 символов")
print("Результат вывода условия:", len(flag))
if len(flag) != 29:
    abort()
print("-" * 10)

# 2
print("Условие: flag[17] != 'g'")
print("Результат вывода условия:", flag[17])
flag = "0123456789ABCDEFGgHIKLMNOPRST"
print("Измененное значение:", flag[17])
print(flag)
if flag[17] != 'g':
    abort()
print("-" * 10)

# 3
print("Условие: flag[:5] != 'ugra_'")
print("Результат вывода условия:", flag[:5])
flag = "ugra_56789ABCDEFGgHIKLMNOPRST"
print("Измененное значение:", flag[:5])
print(flag)
if flag[:5] != 'ugra_':
    abort()
print("-" * 10)

# 4
print("Условие: flag[9:3:-2] != 'nta'")
print("Результат вывода условия:", flag[9:3:-2])
flag = "ugra_a6t8nABCDEFGgHIKLMNOPRST"
print("Измененное значение:", flag[9:3:-2])
print(flag)
if flag[9:3:-2] != 'nta':
    abort()
print("-" * 10)

# 5
print("Условие: flag[-2:-15:-3].encode().hex() != '786b737567'")
print("Кодируемые символы", flag[-2:-15:-3])
print("Результат кодирования сиволов",
      flag[-2:-15:-3].encode().hex(),
      "не совпадает с условием, декодируем")
hex_dec = bytes.fromhex('786b737567').decode('utf-8')
print("Декодированная строка", hex_dec)
flag = "ugra_a6t8nABCDEgGguIKsMNkPRxT"
print(flag)
if flag[-2:-15:-3].encode().hex() != '786b737567':
    abort()
print("-" * 10)

# 6
print("Условие: int.from_bytes(flag[6:18:2].encode(), 'little') != 104927802781555")
print("Кодируемые символы:", flag[6:18:2])
print("Результат кодирования сиволов",
      int.from_bytes(flag[6:18:2].encode(), "little"),
      "не совпадает с условием, декодируем")
int_v = 104927802781555
bytes_string = int_v.to_bytes(6, "little")
print("Декодированная последовательность 104927802781555 ->", bytes_string.decode())
flag = "ugra_astoniBhDng_guIKsMNkPRxT"
print(flag)
if int.from_bytes(flag[6:18:2].encode(), "little") != 104927802781555:
    abort()
print("-" * 10)

# 7
print("Условие: сумма значений по циклу, в котором от символа берется числовое представление и "
      "умножается на 1000 в степени индекса числа. Сумма такого представления равна = 107056052115119102")
print("Кодируемые символы:", flag[19:-4])
value = "107056052115119102"
value_reverse = []
for i in range(0, len(str(value)), 3):
     char_ = f"{value[i]}{value[i+1]}{value[i+2]}"
     value_reverse.append([char_, chr(int(char_))])
print("Декодированная последовательность:", value_reverse)
print("Записывать необходимо в обратном порядке, так как индексы начинаются с 0 [0, 1, 2, 3, 4]")
flag = "ugra_astoniBhDng_gufws48kPRxT"
print(flag)
if sum(ord(x) * 1000 ** i for i, x in enumerate(flag[19:-4])) != 107056052115119102:
    abort()
print("-" * 10)

# 8
print("Условие: base64.b64encode(flag[-4:].encode()) != b'OW14cg=='")
print("Кодируемая последовательность", flag[-4:].encode())
base64_bytes_reverse = b'OW14cg=='
print("декодируем b'OW14cg==':", base64.b64decode(base64_bytes_reverse))
flag = "ugra_astoniBhDng_gufws48k9mxr"
print(flag)
if base64.b64encode(flag[-4:].encode()) != b'OW14cg==':
    abort()

# 9
print("Условие: hashlib.sha256(flag.encode()).hexdigest() должно быть равно = "
      "c03d442919809592c613752762555c6cd46c5d39b5ba8dbfaf4c617533b28bb7")
print("Так как в нашем флаге есть 2 символа, которые мы не трогали 'B' и 'D', необходимо написать "
      "цикл перебора последовательности заменяя их")

flag2 = "ugra_astoniBhDng_gufws48k9mxr"
hex_sha256 = 'c03d442919809592c613752762555c6cd46c5d39b5ba8dbfaf4c617533b28bb7'
for c in (chr(i) for i in range(32, 127)):
    x = flag2.replace('B', c)
    for c2 in (chr(i) for i in range(32, 127)):
        z = x.replace('D', c2)
        if hashlib.sha256(z.encode()).hexdigest() == 'c03d442919809592c613752762555c6cd46c5d39b5ba8dbfaf4c617533b28bb7':
            print("-" * 10)
            print("Искомый флаг:", z)
            flag = z

if hashlib.sha256(flag.encode()).hexdigest() != 'c03d442919809592c613752762555c6cd46c5d39b5ba8dbfaf4c617533b28bb7':
    abort()

print("-" * 10)
print("OK!")
