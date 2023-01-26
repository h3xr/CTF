list_ = []
with open("misc-access.log") as file:
    for line in sorted(file):
        list_.append(line[148])

str_ = ''.join(list_)
print(str_)

result = str_.find('KCTF')
if result:
     print(str_[result:])